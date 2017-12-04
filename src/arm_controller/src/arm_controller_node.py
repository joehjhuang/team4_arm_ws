#!/usr/bin/env python


import numpy as np
import arm_library
import dynamixel_node
import sea_node
import time


class PositionController():
    def __init__(self): 
        self.Dyn = dynamixel_node.DynamixelController()
        self.SEA = sea_node.SEAController()

        np.set_printoptions(precision=20)  
        ft_to_m = 0.3048
        in_to_ft = float(1)/float(12)
        
        l = np.array([12,12,4.5]) * in_to_ft * ft_to_m
        th = self.getCurrentAngles('do not update Arm Object')

        self.Arm = arm_library.Arm(l,th)


   
   

    def movePosition(self,coord):
        coord[2] += np.pi/2
        th = self.Arm.x_to_th(coord)
        print "coord: ", coord, ", th: ",th
        self.getCurrentPosition()
        self.Dyn.rotateArm([th[1],th[2]])
    
    def getCurrentAngles(self,update=False):
        th0 = self.SEA.getAngle()
        d = self.Dyn.getCurrentAngles()
        th = np.array([th0+np.pi/2,-d[0],-d[1]])
        if update == False:
            self.Arm.update_theta(th)
        return th

    def getCurrentPosition(self):
        th = self.getCurrentAngles()
        return self.Arm.th_to_x(th)
    
    def changeOrientation(self,phi):
        curr_coord = self.getCurrentPosition()
        new_coord = [curr_coord[0],curr_coord[1],phi]
        self.movePosition(new_coord)
    
    def isMoving(self):
        if self.Dyn.isMoving() and self.SEA.isMoving():
            return True
        return False
        

    def moveAlongLine(self,coord,n = 100):
        curr_coord = self.getCurrentPosition()
        x_pts = list()
        y_pts = list()
        phi = coord[2]
        x0 = curr_coord[0]
        y0 = curr_coord[1]
        x1 = coord[0]
        y1 = coord[1]

        print "x1", x1
        print "x0", x0
        print "y0", y0
        print "y1", y1

        for i in range(1,n+1):
            x_pts.append( x0 + (x1-x0)*i/(n+1) )
            y_pts.append( y0 + (y1-y0)/(x1-x0) * (x_pts[i-1] - x0) )
        x_pts.append(x1)
        y_pts.append(y1)
        print "y_pts", y_pts
        print "x_pts", x_pts
        
        for i in range(0,n+1):
            self.movePosition( np.array([x_pts[i],y_pts[i],phi]) )
            #print "moving... ", i
            time.sleep(0.01)
            while(self.isMoving()):
            	print "waiting... ", i
                pass


    def openGripper(self):
        self.Dyn.openGripper()
        while( self.Dyn.isMoving() ):
            pass
    def closeGripper(self):
        self.Dyn.closeGripper()
        while( self.Dyn.isMoving() ):
            pass

    def threePointSpline(self,coord_list,speed):
        coord0 = coord_list[0]
        coord1 = coord_list[1]
        coord2 = coord_list[2]
        pass

    def towel_traj_1(self,coord_list):
        coord0 = coord_list[0]
        coord1 = coord_list[1]
        x0 = coord0[0]
        y0 = coord0[1]
        x1 = coord1[0]
        y1 = coord1[1]
        x0_mid = float(x1-x0)/2
        y1_mid = float(y1-y0)/2
        pass
         



def main():
    #rospy.init_node("position_mover",anonymous=True)
    #node = PositionController()
    #rospy.spin()
    Pos = PositionController()
    #while(True):
    #    print "Position = ", Pos.getCurrentPosition()
    while(True):
        Pos.closeGripper()
        time.sleep(2)
        Pos.openGripper()
        time.sleep(2)
        Pos.moveAlongLine([0,0.65,0])
        time.sleep(2)
        Pos.moveAlongLine([0,0.4,0])
        time.sleep(2)
        

if __name__ == '__main__':
    main()
    
"""

"""
