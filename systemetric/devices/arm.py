class Arm(object):
    def __init__(self, mbed):
        self._mbed = mbed
        self.lifted = False

    def setLifted(self, lifted, timeout=10.0):
        """Moves the arm to a specified state.

        :param lifted: whether the arm should be lifted (True) or
                       lowered (False)
        :type lifted: bool
        :param timeout: the amount of time after which the operation
                        should time out and raise an exception.
        :type timeout: float or None
        :returns: a bool representing whether the operation succeeded.
        :raises: mbed.Timeout -- if the arm failed to move to the
                                 specified state in time
        """
        if self.lifted != lifted:
            self._mbed.sendCommand('A' + int(lifted), timeout=timeout)
            self.lifted = lifted
        return True
