import numpy as np

class SEAController():
    def __init__(self):
        self.currentAngle = 0

    def getAngle(self):
        #gets angle of sea joint
        return self.currentAngle

    def setAngle(self,angle):
        #sets angle for sea joint to be at
        self.currentAngle = angle

    def isMoving(self):
        #return True if motor is moving, else return False
        return False





def main():
    S = SEAController()
if __name__ == "__main__":
    main()
