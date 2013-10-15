from robot import Robot

class PacBot(Robot):
    def __init__(self, mode):
        self.mbed = Mbed('/dev/ttyACM0', 115200)
        self.vision = VisionShim('/dev/video0')
        self.leftMotor = MotorMbed(self.mbed, 0)
        self.rightMotor = MotorMbed(self.mbed, 1)
        self.motorDriver = BlindMotorDriver(self.leftMotor, self.rightMotor,
                                            1, 1, 1, 1) #right, left, dist, turn

        super(LifterBot, self).__init__(mode)
    def turn(angle):
        self.motorDriver.turn(angle)
    def moveForward(distance):
        self.motorDriver.moveForward(distance)
