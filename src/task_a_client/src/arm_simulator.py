#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Vector3
import numpy as np

class Arm:
    def __init__(self):
        self.pub = rospy.Publisher('/arm/location', Vector3, queue_size = 10)
        self.timer = rospy.Timer(rospy.Duration(0.02), self.callback)
        self.location = np.array([0., 0., 0.])
        self.velocity = np.array([0.01, 0., 0.])

    def callback(self, msg):
        self.location += self.velocity
        location = Vector3(self.location[0], self.location[1], self.location[2])
        self.pub.publish(location)

if __name__ == '__main__':
    rospy.init_node('arm_simulator')
    node = Arm()
    rospy.spin()

