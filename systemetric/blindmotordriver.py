import time
class BlindMotorDriver(object):
    def __init__(self, mbed, leftMotor, rightMotor, 
    leftMotorFactor=1, rightMotorFactor=1, distanceCalibration=1, turnCalibration=1):
        self._mbed = mbed
        self._motorR = rightMotor
        self._motorL = leftMotor
        self.rightMotorFactor = rightMotorFactor
        self.leftMotorFactor = leftMotorFactor
        self.distancecalibration = distanceCalibration
        self.turnCalibration = turnCalibration
    def moveForward(self, distance):    
        """Moves the robot forwards a set amount of time
        (use negative distance for going backwards)    
        input: distance"""
        try:
            if distance < 0: #if the distance is negative, it becomes positive        
                distance = -distance       
                self.motorR.setPower(100*rightMotorFactor)
                self.motorL.setPower(100*leftMotorFactor)
            else:        
                self.motorR.setPower(-100*rightMotorFactor)
                self.motorL.setPower(-100*leftMotorFactor)
            time.sleep(distance*self.distanceCalibration)
        finally:
        self.motorR.setPower(0)
        self.motorL.setPower(0)
    def turn(self, angle):    
        """Turns the robots a set angle assuming it takes 1s to turn 90    
        input: angle"""
        direction = 1
        while angle > 180:        
            angle = angle-360
        while angle < -179:
            angle = angle+360
        if angle < 0:        
            angle = -angle
            direction = -1
        self.motorR.setPower(direction*100*rightMotorFactor)    
        self.motorL.setPower(direction*100*leftMotorFactor)   
        time.sleep(self.turnCalibration*angle/90.)
        self.motorR.setPower(0)    
        self.motorL.setPower(0)
