

import os
import dynamixel
import time
import random
import arm_library
import numpy as np
import rospy

import time


class DynamixelController():
    #INIT--------------------------------------------------------
    def __init__(self):
        self.myIDs = [15,17,18] #update this line to add motors
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
	self.zeroEncoder = [2574,390,0]
        self.zeroPosition = [2*np.pi * x for x in self.zeroEncoder]
        self.maxSpeed = 100
        self.j3_encoder_open = 609
	self.j3_encoder_close = 60
        self.want_angle = [0,0,getAngle(j3_encoder_open)]
        self.want_torque = [0,0,0]
        self.want_speed = [5,5,5]


        self.dyn_pos_sub = rospy.Subscriber('/dyn_pos_cmd', Vector3, self.posCallback, queue_size=1)
        self.dyn_elbow_sub = rospy.Subscriber('/elbow_cmd', Vector3, self.elbowCallback, queue_size=1)
        self.dyn_wrist_sub = rospy.Subscriber('/wrist_cmd', Vector3, self.wristCallback, queue_size=1)
        self.dyn_gripper_sub = rospy.Subscriber('/gripper_cmd', bool, self.gripperCallback, queue_size=1)

        self.dyn_pos_pub = rospy.Publisher("/dyn_pos_info", Vector3kljkkjl,queue_size=1)

    def setSerial(self):
        # Set your serial port accordingly.
        if os.name == "posix":
            portName = "/dev/ttyUSB2"
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
    
    def gripperCallback(self,data):
        if data.data == True:
            self.closeGripper()
        else: 
            self.openGripper()

    def elbowCallback(self,data):
        self.want_angle[0] = data.x
        self.want_speed[0] = data.y
        self.want_torque[0] = data.z
        self.rotateAbs(want_angle,want_speed)

    def elbowCallback(self,data):
        self.want_angle[1] = data.x
        self.want_speed[1] = data.y
        self.want_torque[1] = data.z
        self.rotateAbs(want_angle,want_speed)
        
        


    def posCallback(self,data):
        if data.z == True:
            self.want_angle = [data.x,data.y,getAngle(j3_encoder_close)]
        else:
            self.want_angle = [data.x,data.y,getAngle(j3_encoder_close)]
        self.rotateAbs(self.want_angle)




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
            speed = [self.want_speed[i] for i in range(self.numServos)]   
     
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
        angles = self.getCurrentAngles()
        for i, x in enumerate(deltaPosition):
            angles[i] += x
        self.rotateAbs(angles,speed)

    def getCurrentAngles(self):
        #returns motor angle in radians
        angles = list()
        encoderPos = self.readServos('CurrentPosition') 
        for i, actuator in enumerate(self.myActuators):
            angles.append(self.getAngle(encoder_pos[i],i) )
        return angles

   def getAngle(self,encoder_pos,i):
       encoder_angle = encoder_pos - self.zeroEncoder[i]
       return float(encoder_angle)/float(self.encoderRange[i])*2*np.pi 
   
    
    def isMoving(self):
        #returns true if dynamixels are moving
        return any(self.readServos("Moving"))

    def openGripper():
        self.want_angle[2] = getAngle(j3_encoder_open)
        self.rotateAbs(self,self.want_angle)
    def closeGripper():
        self.want_angle[2] = getAngle(j3_encoder_close)
        self.rotateAbs(self,self.want_angle)
    
    
                          

            
        



def main():
    rospy.init_node("dynamixel_mover",anonymous=True)
    node = DynamixelController()
    rospy.spin()


if __name__ == "__main__":
    main()




