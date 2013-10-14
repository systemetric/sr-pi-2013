class MotorMbed(object):
    def __init__(self, mbed, motorId):
        """Motor attached to mbed

        :param mbed: the Mbed object
        :param motorId: the motor index
        """

        self._mbed = mbed
        self._motorId = motorId

