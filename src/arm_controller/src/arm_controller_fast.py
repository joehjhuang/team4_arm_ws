#!/usr/bin/env python

import rospy
import std_msgs.msg
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32, Bool
import math as m
import numpy as np
from arm_library import Arm
from dynamixel_node import DynamixelController
import time


"""
This class is the ROS arm actuator node, ROS SEA node is not included

Pubish Topics:
    /arm/location: geometry_msgs/Vector3
    /sea/position_cmd: std_msgs/Float32
    /arm/grab: std_msgs/Bool
Subscribe Topics:
    /arm/grab_cmd: std_msgs/Bool
    /arm/velocity_cmd: geometry_msgs/Vector3
    /sea/position: std_msgs/Float32
"""

"""
1. SEA publish data, you will have full robot states after it
2. setup the Arm object and initialize arm state command
3. keep updating grab command and velocity command by subscribed topics
4. for some time step, based on velocity command update arm state command, while in workspace
5. for some time step, update the arm state command based on current real state and command the robot based on arm state command
   and also publish robot state and sea state

A possible different version is to stop the robot command if it takes too long
"""

# joint_state: sea_state, arm_state (all theta), no gripper state
# joint_state: [sea_theta, elbow_theta, wrist_theta]
# grab_cmd: bool of grab or not command
# arm_location: end effector location, no gripper data
# arm_velocity: end effector velocity, no gripper data
# joint_state_ready: should be ready before updating joint_state_cmd
# cmd_ready: should be ready before moving the robot
# dyn_state: arm_state and gripper_state
# action_joint_state: the action to be sent
# action_close_gripper
# action_open_gripper

class ArmController():
    def __init__(self): 
        self.dynamixel_controller = DynamixelController()
        dyn_state = self.dynamixel_controller.getCurrentAngles()

        self.joint_state_ready = False # same as Arm object ready or not
        self.cmd_ready = False
        self.joint_state = np.array([0., dyn_state[0], dyn_state[1]]) # not ready since shoulder position is not set up yet
        self.grab_cmd = not self.dynamixel_controller.isOpen()
        self.arm_velocity_cmd = np.array([0., 0., 0.])

        self.action_joint_state = np.array([0., dyn_state[0], dyn_state[1]]) # have to be initialized with joint state ready
        self.action_close_gripper = False
        self.action_open_gripper = False
        self.prev_time = -1.
        
        ft_to_m = 0.3048
        in_to_ft = float(1)/float(12)
        self.l = np.array([12., 12., 4.5]) * in_to_ft * ft_to_m
        self.speed = 50

        self.action_joint_state_updater = rospy.Timer(rospy.Duration(0.02), self.action_joint_state_update_callback)
        self.action_sent_state_updater = rospy.Timer(rospy.Duration(0.1), self.action_sent_state_update_callback)

        self.sea_state_sub = rospy.Subscriber("/sea/position", Float32, self.sea_setstate_callback, queue_size = 1)
        self.grab_cmd_sub = rospy.Subscriber("/arm/grab_cmd", Bool, self.grab_cmd_callback, queue_size = 1)
        self.arm_velocity_cmd_sub = rospy.Subscriber("/arm/velocity_cmd", Vector3, self.arm_velocity_cmd_callback, queue_size = 1)

        self.sea_cmd_pub = rospy.Publisher("/sea/position_cmd", Float32, queue_size = 1)
        self.arm_location_pub = rospy.Publisher("/arm/location", Vector3, queue_size = 1)

    def sea_setstate_callback(self, msg):
        if not self.joint_state_ready:
            self.joint_state[0] = msg.data
            self.arm = Arm(self.l, self.joint_state.tolist())
            self.joint_state_ready = True
            # initialize the action joint state
            self.action_joint_state[0] = msg.data
            print "joint state is ready!"
        else:
            self.joint_state[0] = msg.data
        return

    def grab_cmd_callback(self, msg):
        if not self.action_open_gripper and not self.action_close_gripper:
            if not msg.data == self.grab_cmd:
                self.grab_cmd = msg.data
                if self.grab_cmd:
                    self.action_close_gripper = True
                    self.action_open_gripper = False
                else:
                    self.action_open_gripper = True
                    self.action_close_gripper = False
        return

    def arm_velocity_cmd_callback(self, msg):
        self.arm_velocity_cmd = np.array([msg.x, msg.y, msg.z])
        return

    def action_sent_state_update_callback(self, msg):
        if self.joint_state_ready:
            dyn_theta = self.dynamixel_controller.getCurrentAngles()
            self.joint_state[1] = dyn_theta[0]
            self.joint_state[2] = dyn_theta[1]
            arm_location = self.arm.th_to_x(self.joint_state.tolist())
            self.arm_location_pub.publish(Vector3(arm_location[0], arm_location[1], arm_location[2]))

        if self.cmd_ready:
            if self.action_close_gripper:
                self.dynamixel_controller.closeGripper()
                while(self.dynamixel_controller.isMoving()):
                    print "closing gripper"
                    pass
                self.action_close_gripper = False
            elif self.action_open_gripper:
                self.dynamixel_controller.openGripper()
                while(self.dynamixel_controller.isMoving()):
                    print "opening gripper"
                    pass
                self.action_open_gripper = False
            else:
                print "move to: ", self.action_joint_state
                self.sea_cmd_pub.publish(Float32(self.action_joint_state[0]))
                self.dynamixel_controller.rotateArm([self.action_joint_state[1], self.action_joint_state[2]])
                while(self.dynamixel_controller.isMoving()):
                    print "moving"
                    pass
        return


    def action_joint_state_update_callback(self, msg):
        if self.joint_state_ready:
            # command the robot arm to move in specific velocity
            curr_time = time.time()
            if self.prev_time < 0.:
                self.prev_time = curr_time
                return
            dt = curr_time - self.prev_time
            self.prev_time = curr_time

            prev_arm_location = self.arm.th_to_x(self.action_joint_state)
            new_arm_location = [prev_arm_location[0] + self.arm_velocity_cmd[0] * dt,
                    prev_arm_location[1] + self.arm_velocity_cmd[1] * dt,
                    prev_arm_location[2] + self.arm_velocity_cmd[2] * dt]
            if self.arm.x_in_workspace(new_arm_location):
                self.action_joint_state = np.array(self.arm.x_to_th(new_arm_location))
                self.cmd_ready = True
                #print self.action_joint_state
                #print "\n"
            else:
                print "not in workspace"
        return


if __name__ == '__main__':
    rospy.init_node("arm_controller",anonymous=True)
    node = ArmController()
    rospy.spin()
    
    
