#!/usr/bin/env python3
import math
from os import kill
import string
import numpy as np
from yaml import FlowEntryToken

import rospy
import tf
from std_msgs.msg import Int16
from std_msgs.msg import Float64
from std_msgs.msg import Float64
from std_msgs.msg import Empty
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String
from mavros_msgs.msg import OverrideRCIn
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Imu
#from waterlinked_a50_ros_driver.msg import DVL
#from waterlinked_a50_ros_driver.msg import DVLBeam
from sensor_msgs.msg import FluidPressure
from sensor_msgs.msg import LaserScan
from mavros_msgs.srv import CommandLong
from geometry_msgs.msg import Twist
import time
import sys
import argparse

# ---------- Global Variables ---------------

set_mode = [0]*3
set_mode[0] = True   # Mode manual
set_mode[1] = False  # Mode automatic without correction
set_mode[2] = False  # Mode with correction

#Conditions
init_a0 = True
init_p0 = True
arming = False

angle_wrt_startup = [0]*3
angle_roll_a0 = 0.0
angle_pitch_a0 = 0.0
angle_yaw_a0 = 0.0
depth_wrt_startup = 0
depth_p0 = 0

desired_point_vs = [0,0]

enable_depth = False 
enable_ping = True 
pinger_confidence = 0
pinger_distance = 0

Vmax_mot = 1900
Vmin_mot = 1100

# Linear/angular velocity 
u = 0               # linear surge velocity 
v = 0               # linear sway velocity
w = 0               # linear heave velocity 

p = 0               # angular roll velocity
q = 0               # angular pitch velocity 
r = 0               # angular heave velocity 

# ---------- Functions---------------

def joyCallback(data):
	global arming
	global set_mode
	global init_a0
	global init_p0
	global Sum_Errors_Vel
	global Sum_Errors_angle_yaw
	global Sum_Errors_depth

	# Joystick buttons
	btn_arm = data.buttons[7]  # Start button
	btn_disarm = data.buttons[6]  # Back button
	btn_manual_mode = data.buttons[3]  # Y button
	btn_automatic_mode = data.buttons[2]  # X button
	btn_corrected_mode = data.buttons[0]  # A button

	# Disarming when Back button is pressed
	if (btn_disarm == 1 and arming == True):
		arming = False
		armDisarm(arming)

	# Arming when Start button is pressed
	if (btn_arm == 1 and arming == False):
		arming = True
		armDisarm(arming)

	# Switch manual, auto and correction mode
	if (btn_manual_mode and not set_mode[0]):
		set_mode[0] = True
		set_mode[1] = False
		set_mode[2] = False		
		rospy.loginfo("Mode manual")
	if (btn_automatic_mode and not set_mode[1]):
		set_mode[0] = False
		set_mode[1] = True
		set_mode[2] = False		
		rospy.loginfo("Mode automatic")
	if (btn_corrected_mode and not set_mode[2]):
		init_a0 = True
		init_p0 = True
		# set sum errors to 0 here, ex: Sum_Errors_Vel = [0]*3
		set_mode[0] = False
		set_mode[1] = False
		set_mode[2] = True
		rospy.loginfo("Mode correction")

def armDisarm(armed):
	# This functions sends a long command service with 400 code to arm or disarm motors
	if (armed):
		rospy.wait_for_service('mavros/cmd/command')
		try:
			armService = rospy.ServiceProxy('mavros/cmd/command', CommandLong)
			armService(0, 400, 0, 1, 0, 0, 0, 0, 0, 0)
			rospy.loginfo("Arming Succeeded")
		except rospy.ServiceException as e:
			rospy.loginfo("Except arming")
	else:
		rospy.wait_for_service('mavros/cmd/command')
		try:
			armService = rospy.ServiceProxy('mavros/cmd/command', CommandLong)
			armService(0, 400, 0, 0, 0, 0, 0, 0, 0, 0)
			rospy.loginfo("Disarming Succeeded")
		except rospy.ServiceException as e:
			rospy.loginfo("Except disarming")	


def velCallback(cmd_vel):
	global set_mode

	# Only continue if manual_mode is enabled
	if (set_mode[1] or set_mode[2]):
		return

	# Extract cmd_vel message
	roll_left_right 	= mapValueScalSat(cmd_vel.angular.x)
	yaw_left_right 		= mapValueScalSat(-cmd_vel.angular.z)
	ascend_descend 		= mapValueScalSat(cmd_vel.linear.z)
	forward_reverse 	= mapValueScalSat(cmd_vel.linear.x)
	lateral_left_right 	= mapValueScalSat(-cmd_vel.linear.y)
	pitch_left_right 	= mapValueScalSat(cmd_vel.angular.y)

	setOverrideRCIN(pitch_left_right, roll_left_right, ascend_descend, yaw_left_right, forward_reverse, lateral_left_right)

def pingerCallback(data):
	global pinger_confidence
	global pinger_distance

	pinger_distance = data.data[0]
	pinger_confidence = data.data[1]

def OdoCallback(data):
	global angle_roll_a0
	global angle_pitch_a0
	global angle_yaw_a0
	global angle_wrt_startup
	global init_a0
	global p
	global q
	global r

	orientation = data.orientation
	angular_velocity = data.angular_velocity

	# extraction of yaw angle
	q = [orientation.x, orientation.y, orientation.z, orientation.w]
	euler = tf.transformations.euler_from_quaternion(q)
	angle_roll = euler[0]
	angle_pitch = euler[1]
	angle_yaw = euler[2]

	if (init_a0):
		# at 1st execution, init
		angle_roll_a0 = angle_roll
		angle_pitch_a0 = angle_pitch
		angle_yaw_a0 = angle_yaw
		init_a0 = False

	angle_wrt_startup[0] = ((angle_roll - angle_roll_a0 + 3.0*math.pi)%(2.0*math.pi) - math.pi) * 180/math.pi
	angle_wrt_startup[1] = ((angle_pitch - angle_pitch_a0 + 3.0*math.pi)%(2.0*math.pi) - math.pi) * 180/math.pi
	angle_wrt_startup[2] = ((angle_yaw - angle_yaw_a0 + 3.0*math.pi)%(2.0*math.pi) - math.pi) * 180/math.pi
	
	angle = Twist()
	angle.angular.x = angle_wrt_startup[0]
	angle.angular.y = angle_wrt_startup[1]
	angle.angular.z = angle_wrt_startup[2]

	pub_angle_degre.publish(angle)

	# Extraction of angular velocity
	p = angular_velocity.x
	q = angular_velocity.y
	r = angular_velocity.z

	vel = Twist()
	vel.angular.x = p
	vel.angular.y = q
	vel.angular.z = r
	pub_angular_velocity.publish(vel)

	# Only continue if manual_mode is disabled
	if (set_mode[0]):
		return

	# Send PWM commands to motors
	# yaw command to be adapted using sensor feedback	
	Correction_yaw = 1500 
	setOverrideRCIN(1500, 1500, 1500, Correction_yaw, 1500, 1500)


def DvlCallback(data):
	global set_mode
	global u
	global v
	global w

	u = data.velocity.x  # Linear surge velocity
	v = data.velocity.y  # Linear sway velocity
	w = data.velocity.z  # Linear heave velocity

	Vel = Twist()
	Vel.linear.x = u
	Vel.linear.y = v
	Vel.linear.z = w
	pub_linear_velocity.publish(Vel)

def PressureCallback(data):
	global depth_p0
	global depth_wrt_startup
	global init_p0
	rho = 1000.0 # 1025.0 for sea water
	g = 9.80665

	# Only continue if manual_mode is disabled
	if (set_mode[0]):
		return
	elif (set_mode[1]):
		# Only continue if automatic_mode is enabled
		# Define an arbitrary velocity command and observe robot's velocity
		setOverrideRCIN(1500, 1500, 1500, 1500, 1500, 1500)
		return

	pressure = data.fluid_pressure

	if (init_p0):
		# 1st execution, init
		depth_p0 = (pressure - 101300)/(rho*g)
		init_p0 = False

	depth_wrt_startup = (pressure - 101300)/(rho*g) - depth_p0

	# setup depth servo control here
	# ...

	# update Correction_depth
	Correction_depth = 1500	
	# Send PWM commands to motors
	Correction_depth = int(Correction_depth)
	setOverrideRCIN(1500, 1500, Correction_depth, 1500, 1500, 1500)

def mapValueScalSat(value):
	# Correction_Vel and joy between -1 et 1
	# scaling for publishing with setOverrideRCIN values between 1100 and 1900
	# neutral point is 1500
	pulse_width = value * 400 + 1500

	# Saturation
	if pulse_width > 1900:
		pulse_width = 1900
	if pulse_width < 1100:
		pulse_width = 1100

	return int(pulse_width)


def setOverrideRCIN(channel_pitch, channel_roll, channel_throttle, channel_yaw, channel_forward, channel_lateral):
	# This function replaces setservo for motor commands.
	# It overrides Rc channels inputs and simulates motor controls.
	# In this case, each channel manages a group of motors not individually as servo set

	msg_override = OverrideRCIn()
	msg_override.channels[0] = np.uint(channel_pitch)       # pulseCmd[4]--> pitch	
	msg_override.channels[1] = np.uint(channel_roll)        # pulseCmd[3]--> roll
	msg_override.channels[2] = np.uint(channel_throttle)    # pulseCmd[2]--> heave 
	msg_override.channels[3] = np.uint( channel_yaw)        # pulseCmd[5]--> yaw
	msg_override.channels[4] = np.uint(channel_forward)     # pulseCmd[0]--> surge
	msg_override.channels[5] = np.uint(channel_lateral)     # pulseCmd[1]--> sway
	msg_override.channels[6] = 1500
	msg_override.channels[7] = 1500

	pub_msg_override.publish(msg_override)

def desiredpointcallback(data):
	global desired_point_vs
	desired_point_vs = data.data
	
	'''
	vel = Twist()
	vel.linear.x = 0 #vrobot_vs[0]
	vel.linear.y = 0 #vrobot_vs[1]
	vel.linear.z = 0 #vrobot_vs[2]
	vel.angular.x = 0 #vrobot_vs[3]
	vel.angular.y = 0 #vrobot_vs[4]
	vel.angular.z = 0 #vrobot_vs[5]


	forward_reverse = mapValueScalSat(vel.linear.x)
	lateral_left_right = mapValueScalSat(vel.linear.y)
	ascend_descend = mapValueScalSat(-vel.linear.z)
	roll_left_right = mapValueScalSat(vel.angular.x)
	pitch_left_right = mapValueScalSat(vel.angular.y)
	yaw_left_right = mapValueScalSat(vel.angular.z)

	# Send velocity screw to the low level control
	print(vel)
	setOverrideRCIN(pitch_left_right, roll_left_right, ascend_descend,
	                    yaw_left_right, forward_reverse, lateral_left_right)
	'''

def transform(vcam, homogeneous_transform):
	
	return np.matmul(homogeneous_transform, vcam)
	
def interactionMatrix(currentPoint,Z=1):
	return np.matrix([
		[-1/Z, 0, currentPoint[0]/Z, currentPoint[0]*currentPoint[1], -(1 + currentPoint[0]**2), currentPoint[1]],
		[0, -1/Z, currentPoint[1]/Z, 1 + currentPoint[1]**2, -currentPoint[0]*currentPoint[1], -currentPoint[0]]
	])
	

def trackercallback(data):
	# Get cooridnates of desired and current points
	global desired_point_vs
	current_point_vs = data.data

	# Compute error
	error_vs = np.array([current_point_vs[0] - desired_point_vs[0], current_point_vs[1] - desired_point_vs[1]])

	# Compute interaction matrix
	currentL = interactionMatrix(current_point_vs)

	desiredL = interactionMatrix(desired_point_vs)
	
	mixedL = (currentL + desiredL) / 2.0


    # We use one particular L:
	L = mixedL
	#print(L)

    # Reminder about degrees of freedom and columns of L
    # 0 - sway
    # 1 - heave
    # 2 - surge
    # 3 - pitch
    # 4 - yaw
    # 5 - roll


	# Option 1: delete all degrees of freedom except yaw and heave
	#L = np.delete(L, [0, 2, 3, 5], 1)

	# Options 2: delete all degrees of freedom except sway and heave
	#L = np.delete(L, [2, 3, 4, 5], 1)

	# Options 3: delete all degrees of freedom except sway and y
	#L = np.delete(L, [2, 3, 4, 5], 1)


	lamb = 2
	L_pseudo = np.linalg.pinv(L)


    # Compute velocity of the camera
	vcam_vs = - lamb * np.squeeze(np.array(np.matmul(L_pseudo, error_vs)))
	#print(vcam_vs)
	#print(error_vs)
	

	# Make vcam 6x1 before transforming to robot frame
	# For option 1
	#vcam_vs = np.array([0, vcam_vs[0], 0, 0, vcam_vs[1], 0])

	# For option 2
	#vcam_vs = np.array([vcam_vs[0], vcam_vs[1], 0, 0, 0, 0])

	# Set pitch to zero
	vcam_vs[3] = 0

	# Rotation matrix:
	rRc = np.matrix([[0,0,1.0],
			[1.0,0,0],
			[0,1.0,0]])

	# Skew matrix of the position vector (position of camera in the robot frame):
	skew_pos = np.matrix([
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]
		])


	# Transformation matrix:
	transform_cam_to_robot = np.block([
		[rRc, np.matmul(skew_pos, rRc)],
		[np.zeros((3, 3)), rRc]
		])

    # Transform velocity from camera frame to robot frame
	vrobot_vs = np.squeeze(np.array(transform(vcam_vs, transform_cam_to_robot)))


    # Make velocity screw	
	vel = Twist()
	vel.linear.x = vrobot_vs[0]
	vel.linear.y = vrobot_vs[1]
	vel.linear.z = vrobot_vs[2]
	vel.angular.x = vrobot_vs[3]
	vel.angular.y = vrobot_vs[4]
	vel.angular.z = vrobot_vs[5]


	forward_reverse = mapValueScalSat(vel.linear.x)
	lateral_left_right = mapValueScalSat(vel.linear.y)
	ascend_descend = mapValueScalSat(-vel.linear.z)
	roll_left_right = mapValueScalSat(vel.angular.x)
	pitch_left_right = mapValueScalSat(vel.angular.y)
	yaw_left_right = mapValueScalSat(vel.angular.z)





	# Publish messages
	error_norm = np.linalg.norm(error_vs,ord= 2)
	error_vs_msg = Float64(data = error_norm)
	pub_error_vs.publish(error_vs_msg)

	# vcam_vs_msg = Float64MultiArray(data = vcam_vs)
	# pub_vcam_vs.publish(vcam_vs_msg)

	# vrobot_vs_msg = Float64MultiArray(data = vrobot_vs)
	# pub_vrobot_vs.publish(vrobot_vs_msg)

	# Send velocity screw to the low level control
	#print(vel)
	#print(ascend_descend)
	#print(lateral_left_right)
	setOverrideRCIN(pitch_left_right, roll_left_right, ascend_descend,
	                    yaw_left_right, forward_reverse, lateral_left_right)


def subscriber():
	rospy.Subscriber("joy", Joy, joyCallback)
	rospy.Subscriber("cmd_vel", Twist, velCallback)
	#rospy.Subscriber("mavros/imu/data", Imu, OdoCallback)
	#rospy.Subscriber("mavros/imu/water_pressure", FluidPressure, PressureCallback)
	#rospy.Subscriber("/dvl/data", DVL, DvlCallback)
	rospy.Subscriber("distance_sonar", Float64MultiArray, pingerCallback)
	rospy.Subscriber("desired_point",Float64MultiArray,desiredpointcallback, queue_size=1)
	rospy.Subscriber("tracked_point",Float64MultiArray,trackercallback, queue_size=1)
	



if __name__ == '__main__':
	#armDisarm(False)  # Not automatically disarmed at startup
	rospy.init_node('autonomous_MIR', anonymous=False)
	pub_msg_override = rospy.Publisher("mavros/rc/override", OverrideRCIn, queue_size = 10, tcp_nodelay = True)
	pub_angle_degre = rospy.Publisher('angle_degree', Twist, queue_size = 10, tcp_nodelay = True)
	pub_depth = rospy.Publisher('depth/state', Float64, queue_size = 10, tcp_nodelay = True)

	pub_angular_velocity = rospy.Publisher('angular_velocity', Twist, queue_size = 10, tcp_nodelay = True)
	pub_linear_velocity = rospy.Publisher('linear_velocity', Twist, queue_size = 10, tcp_nodelay = True)

	pub_error_vs = rospy.Publisher("visual_servoing_error",Float64,queue_size=1,tcp_nodelay = True)
	pub_vcam_vs = rospy.Publisher("camera_velocity",Float64MultiArray,queue_size=1,tcp_nodelay = True)
	pub_vrobot_vs = rospy.Publisher("robot_velocity",Float64MultiArray,queue_size=1,tcp_nodelay = True)

	subscriber()

	rospy.spin()
