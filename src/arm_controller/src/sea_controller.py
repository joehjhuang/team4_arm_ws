#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

class SEA_Controller():
    def __init__(self):
        self.time_step = 0.02
        self.position_sub = rospy.Subscriber("/sea/position_cmd", Float32, self.position_callback, queue_size = 1)
        self.position_pub = rospy.Publisher("/sea/position", Float32, queue_size = 1)
        self.sea_status_timer = rospy.Timer(rospy.Duration(self.time_step), self.position_pub_callback)
        self.position = 0.0

    def position_callback(self, msg):
        self.position = msg.data

    def position_pub_callback(self, msg):
        self.position_pub.publish(Float32(self.position))

if __name__ == "__main__":
    rospy.init_node("sea_controller")
    node = SEA_Controller()
    rospy.spin()

