class MotorMbed(object):
    def __init__(self, mbed, motorId):
        """Motor attached to mbed

        :param mbed: the Mbed object
        :param motorId: the motor index
        """

        self._mbed = mbed
        self._motorId = motorId
    
    def __del__(self):
        self.setPower(0)

    def setPower(self, power):
        """Changes the motor power to state
        Input: motorID, state"""
        self._mbed.sendCommand('M{}({})'.format(self._motorId, power))
        
