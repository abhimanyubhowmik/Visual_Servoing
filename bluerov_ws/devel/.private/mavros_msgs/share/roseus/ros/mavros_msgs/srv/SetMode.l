;; Auto-generated. Do not edit!


(when (boundp 'mavros_msgs::SetMode)
  (if (not (find-package "MAVROS_MSGS"))
    (make-package "MAVROS_MSGS"))
  (shadow 'SetMode (find-package "MAVROS_MSGS")))
(unless (find-package "MAVROS_MSGS::SETMODE")
  (make-package "MAVROS_MSGS::SETMODE"))
(unless (find-package "MAVROS_MSGS::SETMODEREQUEST")
  (make-package "MAVROS_MSGS::SETMODEREQUEST"))
(unless (find-package "MAVROS_MSGS::SETMODERESPONSE")
  (make-package "MAVROS_MSGS::SETMODERESPONSE"))

(in-package "ROS")





(intern "*MAV_MODE_PREFLIGHT*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_PREFLIGHT* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_PREFLIGHT* 0)
(intern "*MAV_MODE_STABILIZE_DISARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_STABILIZE_DISARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_STABILIZE_DISARMED* 80)
(intern "*MAV_MODE_STABILIZE_ARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_STABILIZE_ARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_STABILIZE_ARMED* 208)
(intern "*MAV_MODE_MANUAL_DISARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_MANUAL_DISARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_MANUAL_DISARMED* 64)
(intern "*MAV_MODE_MANUAL_ARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_MANUAL_ARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_MANUAL_ARMED* 192)
(intern "*MAV_MODE_GUIDED_DISARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_GUIDED_DISARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_GUIDED_DISARMED* 88)
(intern "*MAV_MODE_GUIDED_ARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_GUIDED_ARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_GUIDED_ARMED* 216)
(intern "*MAV_MODE_AUTO_DISARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_AUTO_DISARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_AUTO_DISARMED* 92)
(intern "*MAV_MODE_AUTO_ARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_AUTO_ARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_AUTO_ARMED* 220)
(intern "*MAV_MODE_TEST_DISARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_TEST_DISARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_TEST_DISARMED* 66)
(intern "*MAV_MODE_TEST_ARMED*" (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(shadow '*MAV_MODE_TEST_ARMED* (find-package "MAVROS_MSGS::SETMODEREQUEST"))
(defconstant mavros_msgs::SetModeRequest::*MAV_MODE_TEST_ARMED* 194)

(defun mavros_msgs::SetModeRequest-to-symbol (const)
  (cond
        ((= const 0) 'mavros_msgs::SetModeRequest::*MAV_MODE_PREFLIGHT*)
        ((= const 80) 'mavros_msgs::SetModeRequest::*MAV_MODE_STABILIZE_DISARMED*)
        ((= const 208) 'mavros_msgs::SetModeRequest::*MAV_MODE_STABILIZE_ARMED*)
        ((= const 64) 'mavros_msgs::SetModeRequest::*MAV_MODE_MANUAL_DISARMED*)
        ((= const 192) 'mavros_msgs::SetModeRequest::*MAV_MODE_MANUAL_ARMED*)
        ((= const 88) 'mavros_msgs::SetModeRequest::*MAV_MODE_GUIDED_DISARMED*)
        ((= const 216) 'mavros_msgs::SetModeRequest::*MAV_MODE_GUIDED_ARMED*)
        ((= const 92) 'mavros_msgs::SetModeRequest::*MAV_MODE_AUTO_DISARMED*)
        ((= const 220) 'mavros_msgs::SetModeRequest::*MAV_MODE_AUTO_ARMED*)
        ((= const 66) 'mavros_msgs::SetModeRequest::*MAV_MODE_TEST_DISARMED*)
        ((= const 194) 'mavros_msgs::SetModeRequest::*MAV_MODE_TEST_ARMED*)
        (t nil)))

(defclass mavros_msgs::SetModeRequest
  :super ros::object
  :slots (_base_mode _custom_mode ))

(defmethod mavros_msgs::SetModeRequest
  (:init
   (&key
    ((:base_mode __base_mode) 0)
    ((:custom_mode __custom_mode) "")
    )
   (send-super :init)
   (setq _base_mode (round __base_mode))
   (setq _custom_mode (string __custom_mode))
   self)
  (:base_mode
   (&optional __base_mode)
   (if __base_mode (setq _base_mode __base_mode)) _base_mode)
  (:custom_mode
   (&optional __custom_mode)
   (if __custom_mode (setq _custom_mode __custom_mode)) _custom_mode)
  (:serialization-length
   ()
   (+
    ;; uint8 _base_mode
    1
    ;; string _custom_mode
    4 (length _custom_mode)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _base_mode
       (write-byte _base_mode s)
     ;; string _custom_mode
       (write-long (length _custom_mode) s) (princ _custom_mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _base_mode
     (setq _base_mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; string _custom_mode
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _custom_mode (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass mavros_msgs::SetModeResponse
  :super ros::object
  :slots (_success ))

(defmethod mavros_msgs::SetModeResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass mavros_msgs::SetMode
  :super ros::object
  :slots ())

(setf (get mavros_msgs::SetMode :md5sum-) "48ecf639e39052f8856a839dcddf826a")
(setf (get mavros_msgs::SetMode :datatype-) "mavros_msgs/SetMode")
(setf (get mavros_msgs::SetMode :request) mavros_msgs::SetModeRequest)
(setf (get mavros_msgs::SetMode :response) mavros_msgs::SetModeResponse)

(defmethod mavros_msgs::SetModeRequest
  (:response () (instance mavros_msgs::SetModeResponse :init)))

(setf (get mavros_msgs::SetModeRequest :md5sum-) "48ecf639e39052f8856a839dcddf826a")
(setf (get mavros_msgs::SetModeRequest :datatype-) "mavros_msgs/SetModeRequest")
(setf (get mavros_msgs::SetModeRequest :definition-)
      "# set FCU mode
#
# Known custom modes listed here:
# http://wiki.ros.org/mavros/CustomModes

# basic modes from MAV_MODE
uint8 MAV_MODE_PREFLIGHT		= 0
uint8 MAV_MODE_STABILIZE_DISARMED	= 80
uint8 MAV_MODE_STABILIZE_ARMED		= 208
uint8 MAV_MODE_MANUAL_DISARMED		= 64
uint8 MAV_MODE_MANUAL_ARMED		= 192
uint8 MAV_MODE_GUIDED_DISARMED		= 88
uint8 MAV_MODE_GUIDED_ARMED		= 216
uint8 MAV_MODE_AUTO_DISARMED		= 92
uint8 MAV_MODE_AUTO_ARMED		= 220
uint8 MAV_MODE_TEST_DISARMED		= 66
uint8 MAV_MODE_TEST_ARMED		= 194

uint8 base_mode		# filled by MAV_MODE enum value or 0 if custom_mode != ''
string custom_mode	# string mode representation or integer
---
bool success		# Mode known/parsed correctly and SET_MODE are sent

")

(setf (get mavros_msgs::SetModeResponse :md5sum-) "48ecf639e39052f8856a839dcddf826a")
(setf (get mavros_msgs::SetModeResponse :datatype-) "mavros_msgs/SetModeResponse")
(setf (get mavros_msgs::SetModeResponse :definition-)
      "# set FCU mode
#
# Known custom modes listed here:
# http://wiki.ros.org/mavros/CustomModes

# basic modes from MAV_MODE
uint8 MAV_MODE_PREFLIGHT		= 0
uint8 MAV_MODE_STABILIZE_DISARMED	= 80
uint8 MAV_MODE_STABILIZE_ARMED		= 208
uint8 MAV_MODE_MANUAL_DISARMED		= 64
uint8 MAV_MODE_MANUAL_ARMED		= 192
uint8 MAV_MODE_GUIDED_DISARMED		= 88
uint8 MAV_MODE_GUIDED_ARMED		= 216
uint8 MAV_MODE_AUTO_DISARMED		= 92
uint8 MAV_MODE_AUTO_ARMED		= 220
uint8 MAV_MODE_TEST_DISARMED		= 66
uint8 MAV_MODE_TEST_ARMED		= 194

uint8 base_mode		# filled by MAV_MODE enum value or 0 if custom_mode != ''
string custom_mode	# string mode representation or integer
---
bool success		# Mode known/parsed correctly and SET_MODE are sent

")



(provide :mavros_msgs/SetMode "48ecf639e39052f8856a839dcddf826a")


