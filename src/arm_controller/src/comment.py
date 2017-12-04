"""
class DynamixelController:
    def __init__():
        initialize the dynamixel motors, everything built in
        Input:
            No Input
        Output:
            No Output

    def rotateArm(theta):
        rotate the dynamixel motors to specific angles
        Input:
            theta: list of 2 float; the angle of elbow and wrist
        Output:
            No Outuput

    def getCurrentAngles():
        get the absolute dynamixel motor angles
        Input:
            No Input
        Output:
            angles: list 3 of float; absolute angle in radians of elbow, wrist, gripper

    def isMoving():
        check if dynamixel is moving or not
        Input:
            No Input
        Output:
            is_moving: bool; is the whole dynamixel moving? used for sending another signal

    def openGripper():
        tell the dynamixel to open the gripper
        Input:
            No Input
        Output:
            No Output

    def closeGripper():
        tell the dynamixel to close the gripper
        Input:
            No Input
        Output:
            No Output
"""

"""
class Arm:
    def __init__(l, theta):
        initialize the arm
        Input:
            l: list 3 of float; three lengths of robot arm
            theta: list 3 of float; three initial angle of robot arm
        Output:
            No Output

    def x_to_th(x):
        given (x,y,Phi) of end effector, return the joint angle closest to current joint angle
        Input:
            x: list 3 of float; (x, y, Phi) of the end effector
        Output:
            theta: list 3 of float; the joint angles shoulder, elbow, wrist in radians

    def update_theta(theta):
        update the theta in arm object
        Input:
            theta: list of 3 float; (shoulder, elbow, wrist) in radians
        Output:
            No Output

    def th_to_x(th):
        given (shoulder, elbow, wrist) angleof end effector, return the end effector position
        Input:
            theta: list 3 of float; the joint angles shoulder, elbow, wrist in radians
        Output:
            x: list 3 of float; (x, y, Phi) of the end effector
            
    def get_x():
        get the (x,y,Phi) of the end effector
        Input:
            No Input
        Output:
            x: list of float; (x, y, Phi) of the end effector
"""
