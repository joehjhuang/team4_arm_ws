#! /usr/bin/env python

import rospy
import actionlib
import a_a_action_server.msg

def task_a_client():
    client = actionlib.SimpleActionClient('a_a_action_server', a_a_action_server.msg.a_aAction)
    print "before server"
    client.wait_for_server()
    print "server found"
    goal = a_a_action_server.msg.a_aGoal()
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()


if __name__ == '__main__':
    try:
        rospy.init_node('task_a_client')
        result = task_a_client()
        print result.succeed
    except rospy.ROSInterruptException:
        print "program interrupted"
