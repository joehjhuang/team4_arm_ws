import os
import dynamixel
import time
import random
import arm_library
import numpy as np

import time


class DynamixelController():
    #INIT--------------------------------------------------------
    def __init__(self):
        self.myIDs = [15,29] #update this line to add motors
        self.minServo = min(self.myIDs)-1 
        self.maxServo = max(self.myIDs)+1
        self.numServos = len(self.myIDs)
        
        # A list to hold the dynamixels
        self.myActuators = [0 for _ in range(self.numServos)]
        
        #set serial port
        self.portName = self.setSerial()

        # Default baud rate of the USB2Dynamixel device.
        self.baudRate = 400000

        # Connect to the serial port
        self.serial = self.connectSerial()

	#Setup Net
        self.net = dynamixel.dynamixel_network.DynamixelNetwork( self.serial )

        #Find Dynamixels
        self.findServos()
        print "Actuators = ", self.myActuators

        #initialize Dynamixels
        self.initializeServos()

	#set Dynamixel parameters
	self.encoderRange = [4095,4095]
	self.zeroEncoder = [2574,390]
        self.zeroPosition = [2*np.pi * x for x in self.zeroEncoder]
        self.maxSpeed = 100
        self.servo3encoderOpen = 609
	self.servo3encoderClose = 60

    def setSerial(self):
        # Set your serial port accordingly.
        if os.name == "posix":
            portName = "/dev/ttyUSB0"
        else:
            portName = "COM3"
        return portName

    def connectSerial(self):
        # Connect to the serial port
        print "Connecting to serial port", self.portName, '...',
        serial = dynamixel.serial_stream.SerialStream( port=self.portName, baudrate=self.baudRate, timeout=1)
        print "Connected!"
        return serial

    def findServos(self):
        print "Scanning for Dynamixels...",
        self.net.scan(self.minServo,self.maxServo)
        for dyn in self.net.get_dynamixels():
            try: 
                self.myActuators[ self.myIDs.index(dyn.id) ] = self.net[dyn.id]
            except ValueError:
                 print "Different Servo found with id = ", dyn.id
            print dyn.id,
        if self.numServos <2:
            print "ERROR, Not all servos Connected!"
        else:
            print "...Done, All Servos found"

    def initializeServos(self):
        # Set the default speed and torque
        for actuator in self.myActuators:
            actuator.moving_speed = 100
            actuator.synchronized = True
            actuator.torque_enable = True
            actuator.torque_control_enable = False
            actuator.goal_torque = 0
            actuator.torque_limit = 800
            actuator.max_torque = 800
    #END INIT -----------------------------------------------------
    
    def readOneServo(self,actuator,info):
        #read value of one register of one motor
        actuator.read_all()
        return actuator.cache[dynamixel.defs.REGISTER[info]]
    
    def readServos(self,info):
        values = list()
	for actuator in self.myActuators:
            values.append( self.readOneServo(actuator,info) )
        return values

    def printServoInfo(self,info):
        """
            read values in registers of motors
            input variables: 
                info (string)       
        """
        values = self.readServos(info)
        print info, " = ", values
    
    def rotateAbs(self,position,speed=None):
        #rotates motors to an absolute position
        #position,speed are lists

        if speed==None:
            speed = [self.maxSpeed for _ in range(self.numServos)]   
     
        for p in position:
            if abs(p) > 2*np.pi + 0.1:
                print "angularPosition = ", position
                raise TypeError("abs(angularPosition) > 2pi")
        for i, actuator in enumerate(self.myActuators):
            actuator.moving_speed = speed[i]
            rel_pos = float(position[i])/(2*np.pi)*self.encoderRange[i]
            goal_pos = int(rel_pos + self.zeroEncoder[i])
            count = abs(goal_pos//self.encoderRange[i]) #floor
            if goal_pos < 0:
                actuator.goal_position = goal_pos + self.encoderRange[i]
            elif goal_pos > self.encoderRange[i]:
                actuator.goal_position = goal_pos - self.encoderRange[i]
            else:
                actuator.goal_position = goal_pos
        self.net.synchronize()

    def rotateRel(self,deltaPosition,speed=None):
        #rotates motors to an relative position
        #deltaPosition,speed are lists
        angles = self.getAngles()
        for i, x in enumerate(deltaPosition):
            angles[i] += x
        self.rotateAbs(angles,speed)

    def getAngles(self):
        #returns motor angle in radians
        angles = list()
        encoderPos = self.readServos('CurrentPosition') 
        for i, actuator in enumerate(self.myActuators):
            encoder_angle = encoderPos[i] - self.zeroEncoder[i]
            angles.append( float(encoder_angle)/float(self.encoderRange[i])*2*np.pi )
        return angles
    
    def isMoving(self):
        #returns true if dynamixels are moving
        return any(self.readServos("Moving"))
    


def main():
    dyn = DynamixelController()
    while(True):
        a = np.pi/4
        dyn.rotateAbs([a,a])
        while(dyn.isMoving()):
            pass
        dyn.rotateAbs([0,0])
        while(dyn.isMoving()):
            pass


if __name__ == "__main__":
    main()

