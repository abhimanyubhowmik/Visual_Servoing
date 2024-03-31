;; Auto-generated. Do not edit!


(when (boundp 'autonomous_rov::Health)
  (if (not (find-package "AUTONOMOUS_ROV"))
    (make-package "AUTONOMOUS_ROV"))
  (shadow 'Health (find-package "AUTONOMOUS_ROV")))
(unless (find-package "AUTONOMOUS_ROV::HEALTH")
  (make-package "AUTONOMOUS_ROV::HEALTH"))

(in-package "ROS")
;;//! \htmlinclude Health.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass autonomous_rov::Health
  :super ros::object
  :slots (_header _cpu_used _mem_used _v_batt _i_batt _t_internal _p_internal _sw_1 _sw_2 ))

(defmethod autonomous_rov::Health
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:cpu_used __cpu_used) 0.0)
    ((:mem_used __mem_used) 0.0)
    ((:v_batt __v_batt) 0.0)
    ((:i_batt __i_batt) 0.0)
    ((:t_internal __t_internal) 0.0)
    ((:p_internal __p_internal) 0.0)
    ((:sw_1 __sw_1) nil)
    ((:sw_2 __sw_2) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _cpu_used (float __cpu_used))
   (setq _mem_used (float __mem_used))
   (setq _v_batt (float __v_batt))
   (setq _i_batt (float __i_batt))
   (setq _t_internal (float __t_internal))
   (setq _p_internal (float __p_internal))
   (setq _sw_1 __sw_1)
   (setq _sw_2 __sw_2)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:cpu_used
   (&optional __cpu_used)
   (if __cpu_used (setq _cpu_used __cpu_used)) _cpu_used)
  (:mem_used
   (&optional __mem_used)
   (if __mem_used (setq _mem_used __mem_used)) _mem_used)
  (:v_batt
   (&optional __v_batt)
   (if __v_batt (setq _v_batt __v_batt)) _v_batt)
  (:i_batt
   (&optional __i_batt)
   (if __i_batt (setq _i_batt __i_batt)) _i_batt)
  (:t_internal
   (&optional __t_internal)
   (if __t_internal (setq _t_internal __t_internal)) _t_internal)
  (:p_internal
   (&optional __p_internal)
   (if __p_internal (setq _p_internal __p_internal)) _p_internal)
  (:sw_1
   (&optional (__sw_1 :null))
   (if (not (eq __sw_1 :null)) (setq _sw_1 __sw_1)) _sw_1)
  (:sw_2
   (&optional (__sw_2 :null))
   (if (not (eq __sw_2 :null)) (setq _sw_2 __sw_2)) _sw_2)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _cpu_used
    4
    ;; float32 _mem_used
    4
    ;; float32 _v_batt
    4
    ;; float32 _i_batt
    4
    ;; float32 _t_internal
    4
    ;; float32 _p_internal
    4
    ;; bool _sw_1
    1
    ;; bool _sw_2
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _cpu_used
       (sys::poke _cpu_used (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _mem_used
       (sys::poke _mem_used (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _v_batt
       (sys::poke _v_batt (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _i_batt
       (sys::poke _i_batt (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _t_internal
       (sys::poke _t_internal (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _p_internal
       (sys::poke _p_internal (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _sw_1
       (if _sw_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _sw_2
       (if _sw_2 (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _cpu_used
     (setq _cpu_used (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _mem_used
     (setq _mem_used (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _v_batt
     (setq _v_batt (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _i_batt
     (setq _i_batt (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _t_internal
     (setq _t_internal (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _p_internal
     (setq _p_internal (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _sw_1
     (setq _sw_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _sw_2
     (setq _sw_2 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get autonomous_rov::Health :md5sum-) "3759c570a6250d1aa85350125e6ecdda")
(setf (get autonomous_rov::Health :datatype-) "autonomous_rov/Health")
(setf (get autonomous_rov::Health :definition-)
      "Header    header
float32   cpu_used    # percent cpu utilization
float32   mem_used    # percent memory used
float32   v_batt      # volts
float32   i_batt      # amps
float32   t_internal  # degrees C
float32   p_internal  # Pa
bool      sw_1        # on/off
bool      sw_2        # on/off

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

")



(provide :autonomous_rov/Health "3759c570a6250d1aa85350125e6ecdda")


