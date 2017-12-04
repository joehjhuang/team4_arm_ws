import math as m
import numpy as np
from arm_library import Arm
from dynamixel_node import DynamixelController
import time

dc = DynamixelController()
print dc.isMoving()
goal1 = [0., 0.]
goal2 = [0.5, 0.5]
dc.rotateArm(goal1)
while dc.isMoving():
    print "still moving1"
dc.rotateArm(goal2)
while dc.isMoving():
    print "still moving2"



