#! /usr/bin/env python
"""
2.12 Imitation Action Server: Using Hand Controller published topics to imitationally control the robot arm
Prereq:
    setup the hand_controller, please check prereq of handcontroller.py
    setup the robot arm controller, please check prereq of it
    setup the X_MULTIPLIER, Y_MULTIPLIER, THETA_MULTIPLIER from testing
freeze while action is canceled
Joe Huang Nov 2017
"""
import rospy
import actionlib
from std_msgs.msg import Bool
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32, Bool
import math as m
import numpy as np
from arm_library import Arm
from dynamixel_node import DynamixelController
import time


import a_a_action_server.msg

class ImitationAction(object):
    """
    This is an action server node for task A action A
    The node should be named by a_a_action_server
    The action simply command the robot arm to control by human
    Subscribe topics:
        /freeze_bool: std_msgs/Bool; freeze or not; keep publishing until rospy ends
        /release_bool: std_msgs/Bool; release gripper or not; keep publishing until rospy ends
        /hand_control: geometry_msgs/Vector3; angle of hand controller, 0~360; keep publishing until rospy ends
        /arm/grab_cmd: std_msgs/Bool
        /arm/velocity_cmd: geometry_msgs/Vector3
        /sea/position: std_msgs/Float32
    Publish topics:
        /arm/velocity_cmd: geometry_msgs/Vector3; arm velocity command; keep publishing until action canceled
        /arm/grab_cmd: std_msgs/Bool; arm grab command; keep publishing until action canceled
        /sea/position_cmd: std_msgs/Float32
    Action Server:
        a_a_action_server: a_a_action_server/a_aAction
    """
    def __init__(self, name):
        self.X_MULTIPLIER = 0.0002
        self.Y_MULTIPLIER = 0.0002
        self.THETA_MULTIPLIER = 0.0001
        self.ANGLE_THRESHOLD = 30

        self.freeze = True
        self.prev_freeze = True
        self.set_relative = False
        #self.imu_relative

        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_a_action_server.msg.a_aAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        self.dynamixel_controller = DynamixelController()
        self.dyn_ready = False
        dyn_state = self.dynamixel_controller.getCurrentAngles()
        self.dyn_ready = True

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

        # the execute callback function of the action server
        print "action a server started"
        self.freeze_sub = rospy.Subscriber('/freeze_bool', Bool, self.freeze_callback)
        self.release_sub = rospy.Subscriber('/release_bool', Bool, self.release_callback)
        self.control_sub = rospy.Subscriber('/hand_control', Vector3, self.control_callback)
        self.arm_velocity_pub = rospy.Publisher('/arm/velocity_cmd', Vector3, queue_size = 10)
        # velocity command is presented as x,y,theta
        self.arm_grab_pub = rospy.Publisher('/arm/grab_cmd', Bool, queue_size = 10)
        #time.sleep(0.05)


        self.action_joint_state_updater = rospy.Timer(rospy.Duration(0.02), self.action_joint_state_update_callback)
        self.action_sent_state_updater = rospy.Timer(rospy.Duration(0.1), self.action_sent_state_update_callback)

        self.sea_state_sub = rospy.Subscriber("/sea/position", Float32, self.sea_setstate_callback, queue_size = 1)
        self.grab_cmd_sub = rospy.Subscriber("/arm/grab_cmd", Bool, self.grab_cmd_callback, queue_size = 1)
        self.arm_velocity_cmd_sub = rospy.Subscriber("/arm/velocity_cmd", Vector3, self.arm_velocity_cmd_callback, queue_size = 1)

        self.sea_cmd_pub = rospy.Publisher("/sea/position_cmd", Float32, queue_size = 1)
        
        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break
        # pause the arm before action is canceled
        # dynamixel stopping function
        velocity = Vector3(0.,0.,0.)
        self.arm_velocity_pub.publish(velocity)

        self.arm_velocity_cmd_sub.unregister()
        self.freeze_sub.unregister()
        self.release_sub.unregister()
        self.control_sub.unregister()
        self.sea_state_sub.unregister()
        self.grab_cmd_sub.unregister()
        self.action_joint_state_updater.shutdown()
        self.action_sent_state_updater.shutdown()

        print "let me shutdown"
        while not self.dyn_ready:
            pass
        self.dynamixel_controller.close()
        self.freeze = True
        self.prev_freeze = True
        self.set_relative = False
        self.dynamixel_controller = None

        print "action a server ended"

    def freeze_callback(self, msg):
        if msg.data:
            #print "freezes"
            velocity = Vector3(0.,0.,0.)
            self.arm_velocity_pub.publish(velocity)
            self.freeze = True
            self.prev_freeze = True
        else:
            #print "unfreeze"
            if self.prev_freeze:
                self.set_relative = True
            self.freeze = False
            self.prev_freeze = False

    def release_callback(self, msg):
        if msg.data:
            grab = Bool()
            grab.data = False
            self.arm_grab_pub.publish(grab)
        else:
            #print "grab"
            grab = Bool()
            grab.data = True
            self.arm_grab_pub.publish(grab)

    def control_callback(self, msg):
        if self.set_relative:
            self.set_relative = False
            self.imu_relative = [msg.x, msg.y, msg.z]
        if not self.freeze:
            x = self.shift(msg.x - self.imu_relative[0])
            y = self.shift(msg.y - self.imu_relative[1])
            z = self.shift(msg.z - self.imu_relative[2])
            
            # filter the signal
            if x < self.ANGLE_THRESHOLD and x > -self.ANGLE_THRESHOLD:
                x = 0.
            if y < self.ANGLE_THRESHOLD and y > -self.ANGLE_THRESHOLD:
                y = 0.
            if z < self.ANGLE_THRESHOLD and z > -self.ANGLE_THRESHOLD:
                z = 0.

            velocity = Vector3(x * self.X_MULTIPLIER, y * self.Y_MULTIPLIER, z * self.THETA_MULTIPLIER)
            self.arm_velocity_pub.publish(velocity)
        else:
            velocity = Vector3(0.,0.,0.)
            self.arm_velocity_pub.publish(velocity)

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
        print "in callback"
        self.dyn_ready = False
        if self.joint_state_ready:
            dyn_theta = self.dynamixel_controller.getCurrentAngles()
            self.joint_state[1] = dyn_theta[0]
            self.joint_state[2] = dyn_theta[1]
            arm_location = self.arm.th_to_x(self.joint_state.tolist())

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
        self.dyn_ready = True
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

    def shift(self, rel_angle):
        # make the relative angle between -180 to 180
        if rel_angle > 180:
            return rel_angle - 360.
        elif rel_angle < -180:
            return rel_angle + 360.
        else:
            return rel_angle

if __name__ == '__main__':
    rospy.init_node('a_a_action_server')
    server = ImitationAction(rospy.get_name())
    rospy.spin()
