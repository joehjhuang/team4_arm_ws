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

class ArmController():
    def __init__(self): 
        self.dynamixel_controller = DynamixelController()
        # dynamixel theta is the joint angles: elbow, wrist, gripper
        theta = self.dynamixel_controller.getCurrentAngles()
        # sea_position is the shoulder joint angle
        self.angle_ready = False # same as Arm object ready or not
        self.cmd_ready = False
        self.do_close_gripper = False
        self.do_open_gripper = False
        self.prev_time = -1.
        self.theta_queue = np.array([0.,theta[0],theta[1]]) # not ready since shoulder position is not set up yet
        self.grab_cmd = not self.dynamixel_controller.isOpen()
        self.velocity_cmd = np.array([0., 0., 0.])
        
        ft_to_m = 0.3048
        self.l = np.array([1,1,4.5]) * ft_to_m
        self.speed = 50

        self.arm_status_timer = rospy.Timer(rospy.Duration(0.02), self.arm_status_callback)
        self.arm_cmd_timer = rospy.Timer(rospy.Duration(0.1), self.arm_cmd_callback)

        self.sea_sub = rospy.Subscriber("/sea/position", Float32, self.sea_setstate_callback, queue_size = 1)
        self.arm_grab_cmd_sub = rospy.Subscriber("/arm/grab_cmd", Bool, self.grab_setstate_callback, queue_size = 1)
        self.arm_velocity_cmd_sub = rospy.Subscriber("/arm/velocity_cmd", Vector3, self.velocity_setstate_callback, queue_size = 1)

        self.sea_cmd_pub = rospy.Publisher("/sea/position_cmd", Float32, queue_size = 1)
        self.arm_location_pub = rospy.Publisher("/arm/location", Vector3, queue_size = 1)

    def sea_setstate_callback(self, msg):
        if not self.angle_ready:
            self.theta_queue[0] = msg.data
            self.arm = Arm(self.l, self.theta_queue)
            self.angle_ready = True
            print "angle is ready!"
        else:
            self.theta_queue[0] = msg.data
        return

    def grab_setstate_callback(self, msg):
        if not msg.data == self.grab_cmd:
            self.grab_cmd = msg.data
            if self.grab_cmd:
                self.do_close_gripper = True
                self.do_open_gripper = False
            else:
                self.do_open_gripper = True
                self.do_close_gripper = False
        else:
            self.do_close_gripper = False
            self.do_open_gripper = False
        return

    def velocity_setstate_callback(self, msg):
        if self.angle_ready:
            # command the robot arm to move in specific velocity
            curr_time = time.time()
            if self.prev_time < 0.:
                self.prev_time = curr_time
                return
            dt = curr_time - self.prev_time
            self.prev_time = curr_time

            x = self.arm.th_to_x(self.theta_queue)
            x = [x[0] + msg.x * dt,
                    x[1] + msg.y * dt,
                    x[2] + msg.z * dt]
            if self.arm.in_workspace(x):
                print self.theta_queue
                theta = self.arm.x_to_th(x)
                if theta[0] is float('nan') or theta[1] is float('nan') or theta[2] is float('nan'):
                    return
                else:
                    print theta
                    self.sea_theta_cmd = theta[0]
                    self.dyn_theta_cmd = [theta[1], theta[2]]
                    self.cmd_ready = True
                print "\n"

        return

    def arm_cmd_callback(self, msg):
        print "!!!!!!!!!!!!!!!!!!!"
        if self.cmd_ready:
            print "@@@@@@@@@@@@@@"
            if self.do_close_gripper:
                print "grab"
                #self.dynamixel_controller.closeGripper()
                #while(self.dynamixel_controller.isMoving()):
                #    pass
            elif self.do_open_gripper:
                print "release"
                #self.dynamixel_controller.openGripper()
                #while(self.dynamixel_controller.isMoving()):
                #    pass
            else:
                print "move to: ", self.dyn_theta_cmd
                self.dynamixel_controller.rotateArm(self.dyn_theta_cmd)
                while(self.dynamixel_controller.isMoving()):
                    print "still moving"
                    pass
            self.sea_cmd_pub.publish(Float32(self.sea_theta_cmd))
            print "sea move to:", self.sea_theta_cmd
        return


    def arm_status_callback(self, msg):
        if self.angle_ready:
            theta = self.dynamixel_controller.getCurrentAngles()
            self.theta_queue[1] = theta[0]
            self.theta_queue[2] = theta[1]
            x = self.arm.th_to_x(self.theta_queue)

            self.arm_location_pub.publish(Vector3(x[0], x[1], x[2]))
        return


if __name__ == '__main__':
    rospy.init_node("arm_controller",anonymous=True)
    node = ArmController()
    rospy.spin()
    
    
