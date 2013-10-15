class Arm(object):
    def __init__(self, mbed):
        self._mbed = mbed
        self.state = 0

    def setArmState(self, state, timeout=10.0):
        """Moves the arm to a specified state.

        :param state: whether the arm should be state (True) or
                       lowered (False)
        :type state: bool
        :param timeout: the amount of time after which the operation
                        should time out and raise an exception.
        :type timeout: float or None
        :returns: a bool representing whether the operation succeeded.
        :raises: mbed.Timeout -- if the arm failed to move to the
                                 specified state in time
        """
        if self.state != state:
            self._mbed.sendCommand('A' + int(state), timeout=timeout)
            self.state = state
        return True
