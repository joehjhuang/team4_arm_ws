#! /usr/bin/env python
import rospy
import actionlib

import a_a_action_server.msg
class ImitationAction(object):
    """
    This is an action server node for task A action A
    The node should be named by a_a_action_server
    The action simply command the robot arm to control by human
    """

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_a_action_server.msg.a_aAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break
if __name__ == '__main__':
    rospy.init_node('a_a_action_server')
    server = ImitationAction(rospy.get_name())
    rospy.spin()
