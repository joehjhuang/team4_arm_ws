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
    Publish topics:
        /arm/velocity_cmd: geometry_msgs/Vector3; arm velocity command; keep publishing until action canceled
        /arm/grab_cmd: std_msgs/Bool; arm grab command; keep publishing until action canceled
    Action Server:
        a_a_action_server: a_a_action_server/a_aAction
    """
    def __init__(self, name):
        self.X_MULTIPLIER = 0.01
        self.Y_MULTIPLIER = 0.01
        self.THETA_MULTIPLIER = 0.1
        self.ANGLE_THRESHOLD = 45
        self.freeze = True
        self.prev_freeze = True

        self.set_relative = False
        #self.imu_relative
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_a_action_server.msg.a_aAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        # the execute callback function of the action server
        print "action a server started"
        freeze_sub = rospy.Subscriber('/freeze_bool', Bool, self.freeze_callback)
        release_sub = rospy.Subscriber('/release_bool', Bool, self.release_callback)
        control_sub = rospy.Subscriber('/hand_control', Vector3, self.control_callback)
        self.arm_velocity_pub = rospy.Publisher('/arm/velocity_cmd', Vector3, queue_size = 10)
        # velocity command is presented as x,y,theta
        self.arm_grab_pub = rospy.Publisher('/arm/grab_cmd', Bool, queue_size = 10)
        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break
        # pause the arm before action is canceled
        velocity = Vector3(0.,0.,0.)
        self.arm_velocity_pub.publish(velocity)

        freeze_sub.unregister()
        release_sub.unregister()
        control_sub.unregister()
        print "action a server ended"

    def freeze_callback(self, msg):
        print msg
        if msg.data:
            print "freezes"
            velocity = Vector3(0.,0.,0.)
            self.arm_velocity_pub.publish(velocity)
            self.freeze = True
            self.prev_freeze = True
        else:
            print "unfreeze"
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
            print "grab"
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
