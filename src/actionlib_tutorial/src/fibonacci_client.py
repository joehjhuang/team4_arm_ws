#! /usr/bin/env python

import rospy
import actionlib
import actionlib_tutorial.msg

def fibonacci_client():
    client = actionlib.SimpleActionClient('fibonacci', actionlib_tutorial.msg.FibonacciAction)
    print "before server"
    client.wait_for_server()
    print "find_server"
    goal = actionlib_tutorial.msg.FibonacciGoal(order=20)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('fibonacci_client_py')
        result = fibonacci_client()
        print result.sequence
    except rospy.ROSInterruptException:
        print "program interrupted"
