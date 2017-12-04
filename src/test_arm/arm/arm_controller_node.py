#!/usr/bin/env python

##import rospy
import std_msgs.msg
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64
import rospy
import math as m
import numpy as np
import arm_library


class PositionController():
    def __init__(self): 
        #angular_pos
        self.angle_ready = False #angle data available? 
        self.next_position = False
        
        ft_to_m = 0.3048
        l = np.array([1,1,4.5]) * 0.3048
        th = np.array([0,0,0])
        self.Arm = arm_library.Arm(l,th)
        self.gripper = 0 # 0 = open, 1 = closed
        self.speed = 50
        
        self.pos_queue = np.array([False,False,False])


        self.sea_sub = rospy.Subscriber("/sea_info", Vector3,self.seaPosCallback,queue_size=1)
        self.dyn_pos_sub = rospy.Subscriber("/dyn_pos_info", Vector3,self.dynPosCallback,queue_size=1)
        self.move_pos_sub = rospy.Subscriber("/move_pos",Vector3, self.movePosCallback,queue_size =1)
        self.speed_sub(rospy.Subscriber("/set_speed",Float64, self.setSpeedCallback,queue_size =1)

        self.sea_pub = rospy.Publisher('/sea_cmd', Vector3, queue_size=1)
        self.dyn_pos_pub = rospy.Publisher('/dyn_pos_cmd', Vector3, queue_size=1)
        self.dyn_elbow_pub = rospy.Publisher('/elbow_cmd', Vector3, queue_size=1)
        self.dyn_wrist_pub = rospy.Publisher('/wrist_cmd', Vector3, queue_size=1)
        self.dyn_gripper_pub = rospy.Publisher('/gripper_cmd', bool, queue_size=1)


    #End Init ------------------------------------------

    def setSpeedCallback(self,data):
        self.speed = data.data        

    def seaPosCallback(self,data):
        self.pos_queue[0] = data.x
        if np.all(self.pos_queue): 
            self.Arm.update_theta(self.pos_queue)
            self.pos_queue = np.array([False,False,False])

    def dynPosCallback(self,data):
        self.pos_queue[1] = data.x
        self.pos_queue[2] = data.y
        if np.all(self.pos_queue): 
            self.Arm.update_theta(self.pos_queue)
            self.pos_queue = np.array([False,False,False])

    def movePosCallback(self,data):
        new_pos = np.array([data.x,data.y,data.z])
        self.movePosition(new_pos,self.speed)


    
    def moveForward(self,distance,speed):
        pass
    def moveBackward(self,distance,speed):
        pass
    def moveRight(self,distance,speed):
        pass
    def moveLeft(self,distance,speed):
        pass
    def movePosition(self,coord,speed):
        th = Arm.x_to_th(coord)
        self.sea_pub.publish(Vector3(th[0],None,None)
        self.dyn_pos_pub.publish(Vector3(th[1],th[2],self.gripper)
        
        
    def openGripper(self,coord):
        pass
    def closeGripper(self,coord):
        pass
    def threePointSpline(self,coord_list,speed):
        pass


def main():
    rospy.init_node("position_mover",anonymous=True)
    node = PositionController()
    rospy.spin()
if __name__ == '__main__':
    main()
    
    
