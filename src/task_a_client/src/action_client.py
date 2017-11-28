#! /usr/bin/env python

import rospy
import actionlib
import a_a_action_server.msg
import a_b_action_server.msg
import a_halt_action_server.msg
from std_msgs.msg import Int16

class Client:
    def __init__(self):
        self.r = rospy.Rate(100.)
        self.sub = rospy.Subscriber('/current_task', Int16, self.callback)
        self.pub = rospy.Publisher('/current_task', Int16, queue_size = 10)
        self.goal_distance = 100.
        self.force = 10.
        self.perform_task = 100
        self.command_task = 100 #no task
        self.halt_client = Halt_Client()
        self.a_client = A_Client()
        self.b_client = B_Client(self.force, self.goal_distance)
        # halt while not doing other thing
        self.halt_client.start()
        while not rospy.is_shutdown():
            if self.perform_task != self.command_task:
                # have to switch task
                # kill the current task first
                if self.perform_task == 0:
                    self.a_client.cancel()
                elif self.perform_task == 1:
                    self.b_client.cancel()
                else:
                    self.halt_client.cancel()
                # run the next task
                self.perform_task = self.command_task
                if self.perform_task == 0:
                    self.a_client.start()
                elif self.perform_task == 1:
                    self.b_client.start()
                else:
                    self.halt_client.start()
            else:
                # check status, only action b have to be checked
                if self.perform_task == 1:
                    if self.b_client.is_succeed():
                        print "TASK A ACTION B IS SUCCESSFULLY PERFORMED"
                        # reset to halt task
                        self.pub.publish(Int16(100))
            self.r.sleep()

    def callback(self, msg):
        self.command_task = msg.data
        return

            
class Halt_Client:
    def __init__(self, name = 'a_halt_action_server'):
        self.halt_client = actionlib.SimpleActionClient(name, a_halt_action_server.msg.a_haltAction)

    def start(self):
        self.halt_client.wait_for_server()
        print "halt the robot"
        goal = a_halt_action_server.msg.a_haltGoal()
        self.halt_client.send_goal(goal)
        return

    def cancel(self):
        self.halt_client.cancel_all_goals()
        print "stop halting the robot"
        return

    def is_succeed(self):
        # This action only stop when canceled
        return False
        
class A_Client:
    def __init__(self, name = 'a_a_action_server'):
        self.a_client = actionlib.SimpleActionClient(name, a_a_action_server.msg.a_aAction)

    def start(self):
        self.a_client.wait_for_server()
        print "start performing action a"
        goal = a_a_action_server.msg.a_aGoal()
        self.a_client.send_goal(goal)
        return

    def cancel(self):
        self.a_client.cancel_all_goals()
        print "stop action a"

    def is_succeed(self):
        # This action only stop when canceled
        return False

class B_Client:
    def __init__(self, force, goal_distance, name = 'a_b_action_server'):
        self.b_client = actionlib.SimpleActionClient(name, a_b_action_server.msg.a_bAction)
        self.force = force
        self.goal_distance = goal_distance

    def start(self):
        self.b_client.wait_for_server()
        print "start performing action b"
        goal = a_b_action_server.msg.a_bGoal()
        goal.force = self.force
        goal.goal_distance = self.goal_distance
        self.b_client.send_goal(goal)
        return

    def cancel(self):
        self.b_client.cancel_all_goals()
        print "stop action b"

    def is_succeed(self):
        # This action only stop when canceled
        if self.b_client.get_result() is None:
            return False
        else:
            return True


if __name__ == '__main__':
    rospy.init_node('task_a_client')
    client = Client()
    rospy.spin()
