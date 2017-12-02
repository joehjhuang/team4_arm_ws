#! /usr/bin/env python
"""
2.12 Imitation Action Server: Using Hand Controller published topics to imitationally control the robot arm
Prereq:
    setup the hand_controller, please check prereq of handcontroller.py
    setup the robot arm controller, please check prereq of it
    setup the X_MULTIPLIER, Y_MULTIPLIER, THETA_MULTIPLIER from testing
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
        /freeze_bool: std_msgs/Bool
        /release_bool: std_msgs/Bool
        /hand_controller: geometry_msgs/Vector3
    Publish topics:
        /arm/velocity: geometry_msgs/Vector3
        /arm/grab: std_msgs/Bool
    """
    def __init__(self, name):
        self.X_MULTIPLIER = 0.01
        self.Y_MULTIPLIER = 0.01
        self.THETA_MULTIPLIER = 0.1
        self.freeze = True
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_a_action_server.msg.a_aAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        # the execute callback function of the action server
        print "action a server started"
        freeze_sub = rospy.Subscriber('/freeze_bool', Bool, self.freeze_callback)
        release_sub = rospy.Subscriber('/release_bool', Bool, self.release_callback)
        control_sub = rospy.Subscriber('/hand_control', Vector3, self.control_callback)
        self.arm_velocity_pub = rospy.Publisher('/arm/velocity', Vector3, queue_size = 10)
        # velocity command is presented as x,y,theta
        self.arm_grab_pub = rospy.Publisher('/arm/grab', Bool, queue_size = 10)
        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break
        freeze_sub.unregister()
        release_sub.unregister()
        control_sub.unregister()
        print "action a server ended"

    def freeze_callback(self, msg):
        if msg.data:
            print "freeze"
            velocity = Vector3(0.,0.,0.)
            self.arm_velocity_pub.publish(velocity)
            self.freeze = True
        else:
            self.freeze = False

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
        if not self.freeze:
            x = msg.x * self.X_MULTIPLIER
            y = msg.y * self.Y_MULTIPLIER
            theta = msg.z * self.THETA_MULTIPLIER
            velocity = Vector3(x, y, theta)
            self.arm_velocity_pub.publish(velocity)
        else:
            velocity = Vector3(0.,0.,0.)
            self.arm_velocity_pub.publish(velocity)

if __name__ == '__main__':
    rospy.init_node('a_a_action_server')
    server = ImitationAction(rospy.get_name())
    rospy.spin()
