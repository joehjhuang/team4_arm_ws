#! /usr/bin/env python
import rospy
import actionlib

import a_b_action_server.msg
class PullDrawerAction(object):
    """
    This is an action server node for task A action B
    The node should be named by a_b_action_server
    The action simply command the robot arm to pull the drawer with a specific force to specific distance
    """

    def __init__(self, name):
        self._feedback = a_b_action_server.msg.a_bFeedback()
        self._result = a_b_action_server.msg.a_bResult()
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_b_action_server.msg.a_bAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        force = goal.force
        goal_distance = goal.goal_distance
        moved_distance = 0.
        r =rospy.Rate(1)
        success = True
        while moved_distance <= goal_distance:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                success = False
                break
            moved_distance += force
            self._feedback.moved_distance = moved_distance
            self._as.publish_feedback(self._feedback)
            r.sleep()
        if success:
            self._as.set_succeeded(self._result)
if __name__ == '__main__':
    rospy.init_node('a_b_action_server')
    server = PullDrawerAction(rospy.get_name())
    rospy.spin()
