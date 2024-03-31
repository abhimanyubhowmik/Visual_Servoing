
(cl:in-package :asdf)

(defsystem "autonomous_rov-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Health" :depends-on ("_package_Health"))
    (:file "_package_Health" :depends-on ("_package"))
    (:file "Thruster" :depends-on ("_package_Thruster"))
    (:file "_package_Thruster" :depends-on ("_package"))
  ))