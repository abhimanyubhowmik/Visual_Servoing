;; Auto-generated. Do not edit!


(when (boundp 'autonomous_rov::Thruster)
  (if (not (find-package "AUTONOMOUS_ROV"))
    (make-package "AUTONOMOUS_ROV"))
  (shadow 'Thruster (find-package "AUTONOMOUS_ROV")))
(unless (find-package "AUTONOMOUS_ROV::THRUSTER")
  (make-package "AUTONOMOUS_ROV::THRUSTER"))

(in-package "ROS")
;;//! \htmlinclude Thruster.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass autonomous_rov::Thruster
  :super ros::object
  :slots (_header _commands ))

(defmethod autonomous_rov::Thruster
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:commands __commands) (instance std_msgs::UInt16MultiArray :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _commands __commands)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:commands
   (&rest __commands)
   (if (keywordp (car __commands))
       (send* _commands __commands)
     (progn
       (if __commands (setq _commands (car __commands)))
       _commands)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/UInt16MultiArray _commands
    (send _commands :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/UInt16MultiArray _commands
       (send _commands :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; std_msgs/UInt16MultiArray _commands
     (send _commands :deserialize buf ptr-) (incf ptr- (send _commands :serialization-length))
   ;;
   self)
  )

(setf (get autonomous_rov::Thruster :md5sum-) "ce5410dbe4f7e3f3510d94e3cf5217c2")
(setf (get autonomous_rov::Thruster :datatype-) "autonomous_rov/Thruster")
(setf (get autonomous_rov::Thruster :definition-)
      "Header header
std_msgs/UInt16MultiArray commands

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/UInt16MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
uint16[]            data        # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = \"height\"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = \"width\"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = \"channel\"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension
")



(provide :autonomous_rov/Thruster "ce5410dbe4f7e3f3510d94e3cf5217c2")


