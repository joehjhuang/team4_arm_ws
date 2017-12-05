#!/usr/bin/env python

import numpy as np
import matplotlib as plt



class Arm_Exception(Exception):
     def __init__(self, message):
          self.value = message
     def __str__(self):
          return repr(self.value)
     
class Arm():
     """Robot Arm Object"""
     def __init__(self,l,th):
        self.l = l
        self.th = th
        self.x = self.x_rel()
        self.j_constr_pos = [np.pi/2,np.pi/2,np.pi/2]
        self.j_constr_neg = [0,-np.pi/2,-np.pi/2]


     def J_rel(self,th):
        """Returns the Jacobian using theta relative to arm joints"""
        l = self.l
        j00 = -l[0]*np.sin(th[0])-l[1]*np.sin(th[0]+th[1])-l[2]*np.sin(th[0]+th[1]+th[2])
        j01 = -l[1]*np.sin(th[0]+th[1])-l[2]*np.sin(th[0]+th[1]+th[2])
        j02 = -l[2]*np.sin(th[0]+th[1]+th[2])
        j10 = l[0]*np.cos(th[0])+l[1]*np.cos(th[0]+th[1])+l[2]*np.cos(th[0]+th[1]+th[2])
        j11 = l[1]*np.cos(th[0]+th[1])+l[2]*np.cos(th[0]+th[1]+th[2])
        j12 = l[2]*np.cos(th[0]+th[1]+th[2])
        j20 = 1
        j21 = 1
        j22 = 1
        return np.array([[j00,j01,j02],[j10,j11,j12],[j20,j21,j22]])

     def J_abs(self):
        """Returns Jacobian unp.sin theta relative to inertial frame
          (Only for testing)"""
        l = self.l
        th = self.th
        j00 = -l[0]*np.sin(th[0])
        j01 = -l[1]*np.sin(th[1])
        j02 = -l[2]*np.sin(th[2])
        j10 = l[0]*np.cos(th[0])
        j11 = l[1]*np.cos(th[1])
        j12 = l[2]*np.cos(th[2])
        j20 = 0;
        j21 = 0;
        j22 = 1;
        return np.array([[j00,j01,j02],[j10,j11,j12],[j20,j21,j22]])

     def x_rel(self):
        """Returns end effector position using theta relative to arm joints"""
        return self.th_to_x(self.th)

     def th_to_x(self,th):
        l = self.l
        x = l[0]*np.cos(th[0])+l[1]*np.cos(th[0]+th[1])+l[2]*np.cos(th[0]+th[1]+th[2])
        y = l[0]*np.sin(th[0])+l[1]*np.sin(th[0]+th[1])+l[2]*np.sin(th[0]+th[1]+th[2])
        g = th[0] + th[1] + th[2]
        return np.array([x,y,g])
             

     def x_joints(self):
        """Returns the positions of all joints using theta relative to arm joints"""
        l = self.l
        th = self.th
        x_0 = l[0]*np.cos(th[0])
        x_1 = x_0 + l[1]*np.cos(th[0]+th[1])
        x_2 = x_1 + l[2]*np.cos(th[0]+th[1]+th[2])
        y_0 = l[0]*np.sin(th[0])
        y_1 = y_0 + l[1]*np.sin(th[0]+th[1])
        y_2 = y_1 + l[2]*np.sin(th[0]+th[1]+th[2])
        x_points = np.array([x_0,x_1,x_2])
        y_points = np.array([y_0,y_1,y_2])
        return [x_points,y_points]

        
     def x_abs(self):
        """Returns end effector position using theta relative to inertial frame
          (Only for testing)"""
        l = self.l
        th = self.th
        x = l[0]*np.cos(th[0])+l[1]*np.cos(th[1])+l[2]*np.cos(th[2])
        x = l[0]*np.sin(th[0])+l[1]*np.sin(th[1])+l[2]*np.sin(th[2])
        g = th[2]
        return np.array([x,y,g])

     def moment(self):
        """Returns the moment of the arm for the particular theta"""
        return 0
     
     def torque(self,F):
        l = self.l
        th = self.th
        np.transpose(self.J_rel(self.th))*F

     def get_theta(self):
        return self.th

     def get_length(self):
        return self.l

     def get_x(self):
        return self.x

     def update_theta(self,th):
        self.th = th
        self.x = self.x_rel()

     def update_length(self,l):
        self.l = l

     def update_x(self,x):
        self.th = self.x_to_th(x)
        self.x = x

     def x_in_workspace(self,x):
        """if self.x_rel() in workspace return true"""
        if x[0]**2 + x[1]**2 > sum(self.l)**2 - 0.01:
            return False
        #inv kinematics test
        l = self.l
        X_e = x[0]
        Y_e = x[1]
        Phi_e = x[2]
        Y_c = Y_e - l[2]*np.sin(Phi_e)
        X_c = X_e - l[2]*np.cos(Phi_e)
        alpha = np.arctan2(Y_c,X_c)
        r = (X_c**2 + Y_c**2)**0.5
        inner1 = (l[0]**2+l[1]**2-r**2)/(2*l[0]*l[1])
        if abs(inner1) > 1: 
            return False
        inner2 = (l[0]**2+r**2-l[1]**2)/(2*l[0]*r)
        if abs(inner2) >1:
            return False

        return True

     def x_to_th(self,x):
        """Returns the angle on position for a given x coordinate"""
        if not self.x_in_workspace(x):
             raise Arm_Exception('X not in Workspace')
        l = self.l
        X_e = x[0]
        Y_e = x[1]
        Phi_e = x[2]
        Y_c = Y_e - l[2]*np.sin(Phi_e)
        X_c = X_e - l[2]*np.cos(Phi_e)
        alpha = np.arctan2(Y_c,X_c)
        r = (X_c**2 + Y_c**2)**0.5
        inner1 = (l[0]**2+l[1]**2-r**2)/(2*l[0]*l[1])
        #print "x",x
        #print "inner1", inner1
        #print "l", l
        #print "r", r
        #print "sum(l)",sum(self.l)
        beta = np.arccos( inner1 )
        gamma = np.arccos( (l[0]**2+r**2-l[1]**2)/(2*l[0]*r) )
        #print "beta", beta
        #print "gamma", gamma
        th0 = alpha - gamma
        th1 = np.pi - beta
        th2 = Phi_e - th0 - th1
        
	if th0>self.j_constr_pos[0]:
            th0=self.j_constr_pos[0]
        elif th0<self.j_constr_neg[0]:
            th0=-self.j_constr_neg[0]

        if th1>self.j_constr_pos[1]:
            th1=self.j_constr_pos[1]
        elif th1<self.j_constr_neg[1]:
            th1=-self.j_constr_neg[1]

        if th2>self.j_constr_pos[2]:
            th2=self.j_constr_pos[2]
        elif th2<self.j_constr_neg[2]:
            th2=-self.j_constr_neg[2]
        
        ans = np.array([th0,th1,th2])
        return ans
        


        
        

     def generate_path(self,x_final):
        """Returns a tuple containing angles and angular velocities of path"""
        pass

     def plot_path(self,x_final):
        """Plots angles and angular velocities of path"""
        pass
     
     def th_to_torque(self):
        """Returns the actuator torques for a desired th"""
        pass

     #def plot_arm(self):
        #"""Plots the position of the arm"""
        #joints = self.x_joints
        #plt.plot(joints[0],joints[1])

        
     def th_vel(self,th,x_dot):
         J_inv = np.linalg.inv( self.J_rel(th) )     
         return np.dot(J_inv,x_dot)


class PID():
     def __init__(self,Kp,Ki,Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.lastErr = 0
        self.t = 0
        self.errSum = 0
        
     def update_Kp(self,Kp):
        self.Kp = Kp
        
     def update_Kd(self,Kd):
        self.Kd = Kd
        
     def update_Ki(self,Ki):
        self.Ki = Ki

     def get_Kp(self,Kp):
        return self.Kp
        
     def get_Kd(self,Kd):
        return self.Kd
        
     def get_Ki(self,Ki):
        return self.Ki

     def get_error(self,Goal,Input):
        return Goal-Input

     def dErr(self,error,dt):
        (error - self.lastErr) / dt

     def timeChange(self,t):
        return t - self.t

     def output(self,t,Goal,Input):
        dt = self.timechange(t)
        error = get_error(Goal,Input)
        self.errSum += error*dt
        
        ans = Kp * error + Ki * self.errSum + Kd * dErr(error,dt)
        
        self.t = t
        self.lastErr = error;
        return Kp * error + Ki * errSum + Kd * dErr
        
     
     


            
     

def ft_to_m(ft):
     ft*0.3048
def m_to_ft(m):
     m*3.28084
    
    

class TimeStep():
    """ TimeStep loop will will facilitate events for each time step"""
    pass

def main():
    np.arccos((1+1-2)/(2*1*1))



    th0 = 0.1;
    th1 = 0.1;
    th2 = 0.1;
    l0 = 0.3048;
    l1 = 0.3048;
    l2 = 0.3048 *4.5/12.0;
    f0 = 0;
    f1 = 0;
    F = np.array([f0,f1,0])
    th = np.array([th0,th1,th2]);
    l = np.array([l0,l1,l2]);
    print "l**2" , sum(l)**2
    arm = Arm(l,th)
    #arm.plot_arm()
    #arm.th_vel(th,[0.1,0.1,0.1])
    print "x_to_th close", arm.x_to_th([-0.588156,0.171340,1.73397])
    print ""
    print "x_to_th", arm.x_to_th([-0.688156,0.171340,1.73397])
    print "atan2 sqrt 3" ,np.arctan2(3**0.5,1)
    print "acos 1/2", np.arccos(float(1)/float(2))






if __name__ == '__main__':
    main()



"""General Structure
Class for general arm functions
Class for controlled movement of arm
    -Class for Control
Class to handle operations on each Timestep
Class (main) for testing



        b = 5
        while(b < 4):
            for i,th in enumerate(ans):
                if abs(th) > j_constraint[i] and b == 0:
                    ans2 = self.x_to_th_helper(x,beta = False, gamma = False)
                    break
                if abs(th) > j_constraint and b == 1:
                    ans2 = self.x_to_th_helper(x,beta = True, gamma = False)
                    break
                if abs(th) > j_constraint and b == 2:
                    ans2 = self.x_to_th_helper(x,beta = False, gamma = True)
                    break
                if abs(th) > j_constraint and b == 3:
                    ans2 = self.x_to_th_helper(x,beta = True, gamma = True)
                    break
                ans = ans2
                break
            b +=1
       return ans

    
            
 
    def x_to_th_helper(self,x,beta = True, gamma = True):
        l = self.l
        X_e = x[2]
        Y_e = x[1]
        Phi_e = x[0]
        Y_c = Y_e - l[2]*np.sin(Phi_e)
        X_c = X_e - l[2]*np.cos(Phi_e)
        alpha = np.arctan2(Y_c,X_c)
        r = (X_c**2 + Y_c**2)**0.5
        inner1 = (l[0]**2+l[1]**2-r**2)/(2*l[0]*l[1])
        if beta ==True:
            beta = np.arccos( inner1 )
        elif beta == False:
            beta = -np.arccos( inner1 ) 
        if gamma == True:
            gamma = np.arccos( (l[0]**2+r**2-l[1]**2)/(2*l[0]*r) )
        elif gamma == False:
            gamma = -np.arccos( (l[0]**2+r**2-l[1]**2)/(2*l[0]*r) )
        th0 = alpha - gamma
        th1 = np.pi - beta
        th2 = Phi_e - th0 - th1k,
        return np.array([th0,th1,th2])
"""
