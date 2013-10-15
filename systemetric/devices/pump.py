class Pump(object):
    def __init__(self, mbed):
        self._mbed = mbed
        self.state = False

    def setPumpState(self, state, timeout=10.0):
        """Moves the Pump to a specified state.

        :param state: whether the Pump should be state (True) or
                       lowered (False)
        :type state: bool
        :param timeout: the amount of time after which the operation
                        should time out and raise an exception.
        :type timeout: float or None
        :returns: a bool representing whether the operation succeeded.
        :raises: mbed.Timeout -- if the Pump failed to move to the
                                 specified state in time
        """
        if self.state != state:
            self._mbed.sendCommand('P' + int(state), timeout=timeout)
            self.state = state
        return True
