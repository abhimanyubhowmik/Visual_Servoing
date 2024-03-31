## *********************************************************
##
## File autogenerated for the bluerov package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'x_axis', 'type': 'int', 'default': 1, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'y_axis', 'type': 'int', 'default': 0, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'z_axis', 'type': 'int', 'default': 4, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'wx_axis', 'type': 'int', 'default': 7, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'wy_axis', 'type': 'int', 'default': 6, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'wz_axis', 'type': 'int', 'default': 3, 'level': 0, 'description': '', 'min': 0, 'max': 7, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Left_Stick_X', 'type': 'int', 'value': 0, 'srcline': 42, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Y', 'type': 'int', 'value': 1, 'srcline': 43, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Trigger', 'type': 'int', 'value': 2, 'srcline': 44, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_X', 'type': 'int', 'value': 3, 'srcline': 45, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'left/right', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Y', 'type': 'int', 'value': 4, 'srcline': 46, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'up/down', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Trigger', 'type': 'int', 'value': 5, 'srcline': 47, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Trigger_Pair', 'type': 'int', 'value': 6, 'srcline': 48, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right trigger is positive', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Bumper_Pair', 'type': 'int', 'value': 7, 'srcline': 49, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': 'right bumper is positive', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set axis index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'enable_button', 'type': 'int', 'default': 0, 'level': 0, 'description': '', 'min': 0, 'max': 14, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'A_Button', 'type': 'int', 'value': 0, 'srcline': 54, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'B_Button', 'type': 'int', 'value': 1, 'srcline': 55, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'X_Button', 'type': 'int', 'value': 2, 'srcline': 56, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Y_Button', 'type': 'int', 'value': 3, 'srcline': 57, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Bumper', 'type': 'int', 'value': 4, 'srcline': 58, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Bumper', 'type': 'int', 'value': 5, 'srcline': 59, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Back_Button', 'type': 'int', 'value': 6, 'srcline': 60, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Start_Button', 'type': 'int', 'value': 7, 'srcline': 61, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Power_Button', 'type': 'int', 'value': 8, 'srcline': 62, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Click', 'type': 'int', 'value': 9, 'srcline': 63, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Click', 'type': 'int', 'value': 10, 'srcline': 64, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Left', 'type': 'int', 'value': 11, 'srcline': 65, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Right', 'type': 'int', 'value': 12, 'srcline': 66, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Up', 'type': 'int', 'value': 13, 'srcline': 67, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Down', 'type': 'int', 'value': 14, 'srcline': 68, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set button index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'disable_button', 'type': 'int', 'default': 1, 'level': 0, 'description': '', 'min': 0, 'max': 14, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'A_Button', 'type': 'int', 'value': 0, 'srcline': 54, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'B_Button', 'type': 'int', 'value': 1, 'srcline': 55, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'X_Button', 'type': 'int', 'value': 2, 'srcline': 56, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Y_Button', 'type': 'int', 'value': 3, 'srcline': 57, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Bumper', 'type': 'int', 'value': 4, 'srcline': 58, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Bumper', 'type': 'int', 'value': 5, 'srcline': 59, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Back_Button', 'type': 'int', 'value': 6, 'srcline': 60, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Start_Button', 'type': 'int', 'value': 7, 'srcline': 61, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Power_Button', 'type': 'int', 'value': 8, 'srcline': 62, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Left_Stick_Click', 'type': 'int', 'value': 9, 'srcline': 63, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Right_Stick_Click', 'type': 'int', 'value': 10, 'srcline': 64, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Left', 'type': 'int', 'value': 11, 'srcline': 65, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Right', 'type': 'int', 'value': 12, 'srcline': 66, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Up', 'type': 'int', 'value': 13, 'srcline': 67, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'D_Pad_Down', 'type': 'int', 'value': 14, 'srcline': 68, 'srcfile': '/home/abhimanyu/bluerov_ws/src/autonomous_rov/config/teleop_xbox.config', 'description': '', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to set button index'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'pub_rate', 'type': 'double', 'default': 100.0, 'level': 0, 'description': 'the maximum publish rate', 'min': 0.1, 'max': 200.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'expo', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'improves control at low levels', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'x_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'linear scaling in m/s', 'min': -10.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'y_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'linear scaling in m/s', 'min': -10.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'z_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'linear scaling in m/s', 'min': -10.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'wx_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'angular scaling in rad/s', 'min': -31.4, 'max': 31.4, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'wy_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'angular scaling in rad/s', 'min': -31.4, 'max': 31.4, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'wz_scaling', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'angular scaling in rad/s', 'min': -31.4, 'max': 31.4, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

teleop_xbox_Left_Stick_X = 0
teleop_xbox_Left_Stick_Y = 1
teleop_xbox_Left_Trigger = 2
teleop_xbox_Right_Stick_X = 3
teleop_xbox_Right_Stick_Y = 4
teleop_xbox_Right_Trigger = 5
teleop_xbox_Trigger_Pair = 6
teleop_xbox_Bumper_Pair = 7
teleop_xbox_A_Button = 0
teleop_xbox_B_Button = 1
teleop_xbox_X_Button = 2
teleop_xbox_Y_Button = 3
teleop_xbox_Left_Bumper = 4
teleop_xbox_Right_Bumper = 5
teleop_xbox_Back_Button = 6
teleop_xbox_Start_Button = 7
teleop_xbox_Power_Button = 8
teleop_xbox_Left_Stick_Click = 9
teleop_xbox_Right_Stick_Click = 10
teleop_xbox_D_Pad_Left = 11
teleop_xbox_D_Pad_Right = 12
teleop_xbox_D_Pad_Up = 13
teleop_xbox_D_Pad_Down = 14