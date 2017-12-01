#! /usr/bin/env python
"""
2.12 Halt Action Server: Using Hand Controller published topics to halt the robot arm and stick to the grabbing state
Prereq:
    setup the robot arm controller, please check prereq of it
Joe Huang Nov 2017
"""
import rospy
import actionlib
from geometry_msgs.msg import Vector3

import a_halt_action_server.msg
class HaltAction(object):
    """
    This is an action server node for task A action halt
    The node should be named by a_halt_action_server
    The action simply command the robot arm to halt
    Publish topics:
        /arm/velocity: geometry_msgs/Vector3
    """

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_halt_action_server.msg.a_haltAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        # the execute callback function of the action server
        print "action halt server started"
        r = rospy.Rate(100)
        self.arm_velocity_pub = rospy.Publisher('/arm/velocity', Vector3, queue_size = 10)
        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break
            self.arm_velocity_pub.publish(Vector(0.,0.,0.))
            r.sleep()
        print "action halt server ended"

if __name__ == '__main__':
    rospy.init_node('a_halt_action_server')
    server = HaltAction(rospy.get_name())
    rospy.spin()
