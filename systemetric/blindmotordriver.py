import time
class BlindMotorDriver(object):
    def __init__(self, leftMotor, rightMotor,
                 leftMotorFactor=1, rightMotorFactor=1,
                 distanceCalibration=1, turnCalibration=1):
        self.motorR = rightMotor
        self.motorL = leftMotor
        self.rightMotorFactor = rightMotorFactor
        self.leftMotorFactor = leftMotorFactor
        self.distanceCalibration = distanceCalibration
        self.turnCalibration = turnCalibration
    def moveForward(self, distance):
        """Moves the robot forwards a set amount of time
(use negative distance for going backwards)
input: distance"""
        try:
            if distance < 0: #if the distance is negative, it becomes positive
                distance = -distance
                self.motorR.setPower(100*self.rightMotorFactor)
                self.motorL.setPower(100*self.leftMotorFactor)
            else:
                self.motorR.setPower(-100*self.rightMotorFactor)
                self.motorL.setPower(-100*self.leftMotorFactor)
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
        try:
            self.motorR.setPower(direction*100*self.rightMotorFactor)
            self.motorL.setPower(-direction*100*self.leftMotorFactor)
            time.sleep(self.turnCalibration*angle/90.)
        finally:
            self.motorR.setPower(0)
            self.motorL.setPower(0)
