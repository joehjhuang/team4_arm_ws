#! /usr/bin/env python
"""
2.12 Pull Drawer Action Server: Controlling the robot arm using specific force command and end the action if end effector moved certain distance
Prereq:
    setup the robot arm controller, please check prereq of it
Joe Huang Nov 2017
"""
import rospy
import numpy as np
import actionlib
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3
import a_b_action_server.msg
from arm_library import Arm
from dynamixel_node import DynamixelController
import time
import math as m

class PullDrawerAction(object):
    """
    This is an action server node for task A action B
    The node should be named by a_b_action_server
    The action simply use position control to arm to pull the drawer with a specific velocity
    Subscribe topics:
        /sea/position: std_msgs/Float32
    Publish topics:
        /sea/position_cmd: std_msgs/Float32
    """

    def __init__(self, name):
        self._feedback = a_b_action_server.msg.a_bFeedback()
        self._result = a_b_action_server.msg.a_bResult()
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_b_action_server.msg.a_bAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        print "action b server started"
        self.y_velocity = goal.velocity
        goal_distance = goal.goal_distance

        self.dynamixel_controller = DynamixelController()
        self.dyn_ready = False
        self.dynamixel_controller.closeGripper()
        while(self.dynamixel_controller.isMoving()):
            print "closing gripper"
            pass

        dyn_state = self.dynamixel_controller.getCurrentAngles()
        self.dyn_ready = True
        self.joint_state_ready = False
        self.joint_state = np.array([0., dyn_state[0], dyn_state[1]]) # not ready since shoulder position is not set up yet

        ft_to_m = 0.3048
        in_to_ft = float(1)/float(12)
        self.l = np.array([12., 12., 4.5]) * in_to_ft * ft_to_m
        self.speed = 50

        self.time_step = 0.1
        self.sea_state_sub = rospy.Subscriber("/sea/position", Float32, self.sea_setstate_callback, queue_size = 1)
        self.sea_cmd_pub = rospy.Publisher("/sea/position_cmd", Float32, queue_size = 1)
        self.action_sent_state_updater = rospy.Timer(rospy.Duration(self.time_step), self.action_sent_state_update_callback)

        success = True
        self.moved_distance = 0.
        while self.moved_distance <= goal_distance:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                success = False
                break
            self._feedback.moved_distance = self.moved_distance
            self._as.publish_feedback(self._feedback)
        if success:
            self._as.set_succeeded(self._result)

        self.sea_state_sub.unregister()
        self.action_sent_state_updater.shutdown()

        while not self.dyn_ready:
            pass
        self.dynamixel_controller.close()
        self.dynamixel_controller = None

        print "action b server ended"

    def sea_setstate_callback(self, msg):
        if not self.joint_state_ready:
            self.joint_state[0] = msg.data
            self.arm = Arm(self.l, self.joint_state.tolist())
            self.start_location = self.arm.th_to_x(self.joint_state.tolist())
            self.joint_state_ready = True
            print "joint state is ready!"
        else:
            self.joint_state[0] = msg.data
        return

    def action_sent_state_update_callback(self, msg):
        self.dyn_ready = False
        if self.joint_state_ready:
            dyn_theta = self.dynamixel_controller.getCurrentAngles()
            self.joint_state[1] = dyn_theta[0]
            self.joint_state[2] = dyn_theta[1]
            prev_arm_location = self.arm.th_to_x(self.joint_state.tolist())
            self.moved_distance = np.sqrt((prev_arm_location[0] - self.start_location[0])**2 + (prev_arm_location[1] - self.start_location[1])**2)

            new_arm_location = [prev_arm_location[0],
                    prev_arm_location[1] + self.time_step * self.y_velocity,
                    prev_arm_location[2]]

            action_joint_state = self.joint_state.copy()
            if self.arm.x_in_workspace(new_arm_location):
                action_joint_state = np.array(self.arm.x_to_th(new_arm_location))
            else:
                print "not in workspace"

            self.sea_cmd_pub.publish(Float32(action_joint_state[0]))
            self.dynamixel_controller.rotateArm([action_joint_state[1], action_joint_state[2]])
            while(self.dynamixel_controller.isMoving()):
                print "moving"
                pass
        self.dyn_ready = True
        return

        

if __name__ == '__main__':
    rospy.init_node('a_b_action_server')
    server = PullDrawerAction(rospy.get_name())
    rospy.spin()
