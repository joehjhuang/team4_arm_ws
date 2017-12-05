
import os
import dynamixel
import time
import numpy as np

import time


class DynamixelController():
    #INIT--------------------------------------------------------
    def __init__(self):
        self.myIDs = [15,16,18] #update this line to add motors
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
	self.encoderRange = [4095,4095,1023]
	self.zeroEncoder = [2574,1377,300]
        self.zeroPosition = [2*np.pi * x for x in self.zeroEncoder]
        self.maxSpeed = 20
        self.servo3encoderOpen = 200
	self.servo3encoderClose = 425

        #Angle that we want motor at, gets updated
        self.want_angle = self.getCurrentAngles()
        self.want_speed = [20,20,20]


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
        for i in range(100):
            try:
                serial = dynamixel.serial_stream.SerialStream( port=self.portName, baudrate=self.baudRate, timeout=1) 
                print "Connected!"
                return serial
                break
            except:
                self.portname = "/dev/ttyUSB" + str(i)
        print "Not Connected"

    def close(self):
        self.stop()
        self.serial.close()
        print "successfully close the dynamixel"
  
        
        

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
	"""
            #read values in registers of motors
            input variables: 
                info (string)

	   ('ModelNumber',  0, "Model Number"),
	   ('FirmwareVersion',  2, "Firmware Version"),
	   ('Id', 3, "Id"),
	   ('BaudRate',  4, "Baud Rate"),
	   ('ReturnDelay',  5, "Return Delay"),
	   ('CWAngleLimit',  6, "CW Angle Limit"),
	   ('CCWAngleLimit',  8, "CCW Angle Limit"),
	   ('TemperatureLimit',  11, "Temperature Limit"),
	   ('LowVoltageLimit',  12, "Low Voltage Limit"),
	   ('HighVoltageLimit',  13, "High Voltage Limit"),
	   ('MaxTorque',  14, "Max Torque"),
	   ('StatusReturnLevel',  16, "Status Return Level"),
	   ('AlarmLED',  17, "Alarm Led"),
	   ('AlarmShutdown',  18, "Alarm Shutdown"),
	   ('DownCalibration',  20, "Down Calibration"),
	   ('UpCalibration',  22, "Up Calibration"),
	   ('TorqueEnable',  24, "Torque Enable"),
	   ('LED',  25, "LED"),
	   ('CWComplianceMargin',  26, "CW Compliance Margin"),
	   ('CCWComplianceMargin',  27, "CCW Compliance Margin"),
	   ('CWComplianceSlope',  28, "CW Compliance Slope"),
	   ('CCWComplianceSlope',  29, "CCW Compliance Slope"),
	   ('GoalPosition', 30, "Goal Position"),
	   ('MovingSpeed', 32, "Moving Speed"),
	   ('TorqueLimit',  34, "Torque Limit"),
	   ('CurrentPosition',  36, "Current Position"),
	   ('CurrentSpeed',  38, "Current Speed"),
	   ('CurrentLoad',  40, "Current Load"),
	   ('CurrentVoltage',  42, "Current Voltage"),
	   ('CurrentTemperature',  43, "Current Temperature"),
	   ('RegisteredInstruction',  44, "Registered Instruction"),
	   ('Moving',  46, "Moving"),
	   ('Lock',  47, "Lock"),
	   ('Punch',  48, "Punch" ),
	   ('TorqueControlEnable',  70, "Torque Control Enable" ),
	   ('GoalTorque',  71, "Goal Torque" )])
        """
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
            speed = [x for x in self.want_speed]   
        for p in position:
            if abs(p) > 2*np.pi + 0.1:
                #print "angularPosition = ", position
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
        #print [actuator.goal_position for actuator in self.myActuators]
        self.net.synchronize()
        self.want_angle = position

    def rotateRel(self,deltaPosition,speed=None):
        #rotates motors to an relative position
        #deltaPosition,speed are lists
        angles = self.getCurrentAngles()
        for i, x in enumerate(deltaPosition):
            angles[i] += x
        self.rotateAbs(angles,speed)



    def getCurrentAngles(self):
        #returns motor angle in radians
        angles = list()
        encoder_pos = self.readServos('CurrentPosition') 
        for i, actuator in enumerate(self.myActuators):
            angles.append(self.encoderToRad(encoder_pos[i],i) )
        return angles

    def encoderToRad(self,encoder_pos,i):
       encoder_angle = encoder_pos - self.zeroEncoder[i]
       return float(encoder_angle)/float(self.encoderRange[i])*2*np.pi 
    
    def isMoving(self):
        #returns true if dynamixels are moving
        return any(self.readServos("Moving"))
    
    def closeGripper(self):
        self.want_angle[2] = self.encoderToRad(self.servo3encoderClose,2)
        self.rotateAbs(self.want_angle)
    def openGripper(self):
        self.want_angle[2] = self.encoderToRad(self.servo3encoderOpen,2)
        self.rotateAbs(self.want_angle)

    def rotateArm(self,joints_12):
        #Joints_12 is a 2 parameter vector
        self.want_angle[0] = joints_12[0]
        self.want_angle[1] = joints_12[1]
        #print "self.want_angle",self.want_angle
        self.rotateAbs(self.want_angle)   


    def isOpen(self):
        if self.readOneServo(self.myActuators[2], "CurrentPosition") > self.servo3encoderOpen + 50:
            return False
        return True

    def stop(self):
        for actuator in self.myActuators:
            actuator.stop()



def main():
    dyn = DynamixelController()
    b = True
    #while(True):
        #dyn.printServoInfo("CurrentPosition")
    while(b ==True):
        a = np.pi/2
        dyn.rotateAbs([-a,a,a])
        while(dyn.isMoving()):
           pass
        dyn.rotateAbs([0,0,0])
        while(dyn.isMoving()):
            pass

        dyn.closeGripper()
        while(dyn.isMoving()):
            pass
        dyn.openGripper()
        while(dyn.isMoving()):
            pass
        #b = False






if __name__ == "__main__":
    main()
