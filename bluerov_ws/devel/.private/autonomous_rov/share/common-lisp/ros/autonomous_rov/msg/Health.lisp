; Auto-generated. Do not edit!


(cl:in-package autonomous_rov-msg)


;//! \htmlinclude Health.msg.html

(cl:defclass <Health> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (cpu_used
    :reader cpu_used
    :initarg :cpu_used
    :type cl:float
    :initform 0.0)
   (mem_used
    :reader mem_used
    :initarg :mem_used
    :type cl:float
    :initform 0.0)
   (v_batt
    :reader v_batt
    :initarg :v_batt
    :type cl:float
    :initform 0.0)
   (i_batt
    :reader i_batt
    :initarg :i_batt
    :type cl:float
    :initform 0.0)
   (t_internal
    :reader t_internal
    :initarg :t_internal
    :type cl:float
    :initform 0.0)
   (p_internal
    :reader p_internal
    :initarg :p_internal
    :type cl:float
    :initform 0.0)
   (sw_1
    :reader sw_1
    :initarg :sw_1
    :type cl:boolean
    :initform cl:nil)
   (sw_2
    :reader sw_2
    :initarg :sw_2
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Health (<Health>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Health>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Health)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autonomous_rov-msg:<Health> is deprecated: use autonomous_rov-msg:Health instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:header-val is deprecated.  Use autonomous_rov-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'cpu_used-val :lambda-list '(m))
(cl:defmethod cpu_used-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:cpu_used-val is deprecated.  Use autonomous_rov-msg:cpu_used instead.")
  (cpu_used m))

(cl:ensure-generic-function 'mem_used-val :lambda-list '(m))
(cl:defmethod mem_used-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:mem_used-val is deprecated.  Use autonomous_rov-msg:mem_used instead.")
  (mem_used m))

(cl:ensure-generic-function 'v_batt-val :lambda-list '(m))
(cl:defmethod v_batt-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:v_batt-val is deprecated.  Use autonomous_rov-msg:v_batt instead.")
  (v_batt m))

(cl:ensure-generic-function 'i_batt-val :lambda-list '(m))
(cl:defmethod i_batt-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:i_batt-val is deprecated.  Use autonomous_rov-msg:i_batt instead.")
  (i_batt m))

(cl:ensure-generic-function 't_internal-val :lambda-list '(m))
(cl:defmethod t_internal-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:t_internal-val is deprecated.  Use autonomous_rov-msg:t_internal instead.")
  (t_internal m))

(cl:ensure-generic-function 'p_internal-val :lambda-list '(m))
(cl:defmethod p_internal-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:p_internal-val is deprecated.  Use autonomous_rov-msg:p_internal instead.")
  (p_internal m))

(cl:ensure-generic-function 'sw_1-val :lambda-list '(m))
(cl:defmethod sw_1-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:sw_1-val is deprecated.  Use autonomous_rov-msg:sw_1 instead.")
  (sw_1 m))

(cl:ensure-generic-function 'sw_2-val :lambda-list '(m))
(cl:defmethod sw_2-val ((m <Health>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autonomous_rov-msg:sw_2-val is deprecated.  Use autonomous_rov-msg:sw_2 instead.")
  (sw_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Health>) ostream)
  "Serializes a message object of type '<Health>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'cpu_used))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mem_used))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'v_batt))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'i_batt))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 't_internal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'p_internal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sw_1) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sw_2) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Health>) istream)
  "Deserializes a message object of type '<Health>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'cpu_used) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mem_used) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'v_batt) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'i_batt) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 't_internal) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'p_internal) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'sw_1) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'sw_2) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Health>)))
  "Returns string type for a message object of type '<Health>"
  "autonomous_rov/Health")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Health)))
  "Returns string type for a message object of type 'Health"
  "autonomous_rov/Health")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Health>)))
  "Returns md5sum for a message object of type '<Health>"
  "3759c570a6250d1aa85350125e6ecdda")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Health)))
  "Returns md5sum for a message object of type 'Health"
  "3759c570a6250d1aa85350125e6ecdda")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Health>)))
  "Returns full string definition for message of type '<Health>"
  (cl:format cl:nil "Header    header~%float32   cpu_used    # percent cpu utilization~%float32   mem_used    # percent memory used~%float32   v_batt      # volts~%float32   i_batt      # amps~%float32   t_internal  # degrees C~%float32   p_internal  # Pa~%bool      sw_1        # on/off~%bool      sw_2        # on/off~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Health)))
  "Returns full string definition for message of type 'Health"
  (cl:format cl:nil "Header    header~%float32   cpu_used    # percent cpu utilization~%float32   mem_used    # percent memory used~%float32   v_batt      # volts~%float32   i_batt      # amps~%float32   t_internal  # degrees C~%float32   p_internal  # Pa~%bool      sw_1        # on/off~%bool      sw_2        # on/off~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Health>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Health>))
  "Converts a ROS message object to a list"
  (cl:list 'Health
    (cl:cons ':header (header msg))
    (cl:cons ':cpu_used (cpu_used msg))
    (cl:cons ':mem_used (mem_used msg))
    (cl:cons ':v_batt (v_batt msg))
    (cl:cons ':i_batt (i_batt msg))
    (cl:cons ':t_internal (t_internal msg))
    (cl:cons ':p_internal (p_internal msg))
    (cl:cons ':sw_1 (sw_1 msg))
    (cl:cons ':sw_2 (sw_2 msg))
))
