import serial
import threading

class MbedTimeout(Exception):
    def __init__(self, mbed, command, response, timeout):
        self.mbed = mbed
        self.command = command
        self.response = response
        self.timeout = timeout
    def __str__(self):
        return "{} timed out after {} seconds.\n" \
               "Command: '{}'\n" \
               "Partial Response: '{}'" \
               .format(self.mbed, self.timeout, self.command, self.response)

class Mbed(object):
    """An mbed device, plugged into the Raspberry Pi using USB.

    Uses serial communication over USB.
    """
    def __init__(self,
                 device='/dev/ttyACM0',
                 baudrate=115200):
        """Creates the mbed device.

        :param device: The Linux device name of the mbed
        :param baudrate: The serial baud rate to be used
        :raises: serial.SerialException -- when device not found
        :raises: ValueError -- when baud rate out of range
        """

        self.serial = serial.Serial(device, baudrate)
        self._lock = threading.Lock()
        self.serial.flushInput()

    def __str__(self):
        return "<mbed at '{}', {} baud rate>" \
                .format(self.serial.name, self.serial.baudrate)

    def sendCommand(self, command, timeout=5.0):
        """Sends command to mbed.

        Sends a single command to the mbed, waits for the response
        and returns it. Command cannot contain linebreaks.

        :param command: The single line command to be used.
                        No linebreak necessary.
        :param timeout: The amount of time to wait for a response
                        before giving up
        :type timeout: float or None
        :returns: str -- the mbed response
        :raises: ValueError -- when command contains a linebreak
        :raises: RuntimeError -- when mbed still has unread data in its
                                 buffer
        """

        # we don't want newlines in our command
        if '\n' in command:
            raise ValueError("command cannot contain linebreak")

        with self._lock:
            # we expect there not to be any leftover data from before
            if self.serial.inWaiting() > 0:
                raise RuntimeError("mbed device still has unread data")

            self.serial.flushInput()
            self.serial.write(command)
            self.serial.flush()
            self.serial.timeout, oldTimeout = timeout, self.serial.timeout
            try:
                data = self.serial.readline()
            finally:
                self.serial.timeout = oldTimeout

        # we expect the data to end in a new line
        if data[-1] != '\n':
            raise MbedTimeout(self, timeout, command, data)

        return data.rstrip()

