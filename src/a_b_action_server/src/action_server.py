#! /usr/bin/env python
"""
2.12 Pull Drawer Action Server: Controlling the robot arm using specific force command and end the action if end effector moved certain distance
Prereq:
    setup the robot arm controller, please check prereq of it
Joe Huang Nov 2017
"""
import rospy
import numpy
import actionlib
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3
import a_b_action_server.msg

class PullDrawerAction(object):
    """
    This is an action server node for task A action B
    The node should be named by a_b_action_server
    The action simply command the robot arm to pull the drawer with a specific force to specific distance
    Subscribe topics:
        /arm/location: geometry_msgs/Vector3
    Publish topics:
        /arm/force: std_msgs/Float32
    """

    def __init__(self, name):
        self._feedback = a_b_action_server.msg.a_bFeedback()
        self._result = a_b_action_server.msg.a_bResult()
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, a_b_action_server.msg.a_bAction, execute_cb = self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        print "action b server started"
        self.start_location = None
        location_sub = rospy.Subscriber('/arm/location', Vector3, self.location_callback)
        self.arm_force_pub = rospy.Publisher('/arm/force', Float32, queue_size = 10)
        force = goal.force
        self.arm_force_pub.publish(Float32(force))
        goal_distance = goal.goal_distance
        moved_distance = 0.
        r =rospy.Rate(1)
        success = True
        while moved_distance <= goal_distance:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                success = False
                break
            if self.start_location is None:
                move_distance = 0.
            else:
                move_distance = np.sqrt(np.sum(np.square(self.current_location - self.start_location)))
            self._feedback.moved_distance = moved_distance
            self._as.publish_feedback(self._feedback)
            self.arm_force_pub.publish(Float32(force))
            r.sleep()
        if success:
            self._as.set_succeeded(self._result)
        location_sub.unregister()
        print "action b server ended"

    def location_callback(self, msg):
        self.current_location = np.array([msg.x, msg.y, msg.z])
        if self.start_location is None:
            self.start_location = np.array([msg.x, msg.y, msg.z])
        

if __name__ == '__main__':
    rospy.init_node('a_b_action_server')
    server = PullDrawerAction(rospy.get_name())
    rospy.spin()
