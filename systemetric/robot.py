import logging

def check_requires(obj, things, funcName, className):
    """Check the requirements specified by @requires"""
    for thing in things:
        if not hasattr(obj, thing):
            return ("`{}` object (required by `{c}.{f}`) "
                    "not initialised in {c}"
                    .format(thing, f=funcName, c=className))
    return None

def requires(things, required=False):
    """Decorator factory that implements a requirement system

    Annotates functions that require certain members be present in
    the Robot class

    Use like this::

        @requires(["vision", "visionMode"], required=True):
        def see():
            pass

    :param things:   a list of strings indicating the members that are
                     required by the decorated function.
    :param required: if ``True``, indicates that the member is
                     essential, and marks the member for checking in
                     ``Robot.__init__``. Otherwise, the member is only
                     checked when a function that requires it is called
    """

    def do_decorate(func):
        def decorated(self, *args, **kwargs):
            requiresError = check_requires(self, things, func.__name__,
                                            self.__class__.__name__)
            if requiresError:
                raise RuntimeError(requiresError)
            return func(self, *args, **kwargs)

        decorated._requiresData = (things, required)
        return decorated

    return do_decorate

class Robot(object):
    """Magic Robot base class

    This class is magic. It enables and disables bits of code depending
    on which bits of the robot are present.

    This constructor must be called at the end of a derived class
    constructor. The derived class constructor must first set up
    any bits of the robot that are present and needed, e.g.::

        class DerivedRobot(Robot):
            def __init__(self):
                # set up any bits of the robot here
                # this robot has motors and a pump
                self.motorDriver = MotorDriver()
                self.pump = Pump()

                # we're done setting up
                # call the Robot magic constructor
                super(DerivedRobot, self).__init__()
    """


    def __init__(self):
        """Initialise the magic.

        This constructor must be called at the end of a derived class
        constructor.
        """

        className = self.__class__.__name__
        self.logger = logging.getLogger(className)

        # check requires
        for name in dir(self):
            try:
                method = getattr(self, name)
                things, required = getattr(method, "_requiresData")
            except AttributeError:
                continue
            requiresError = check_requires(self, things, name, className)
            if requiresError:
                if required:
                    raise NotImplementedError("Required " + requiresError)
                else:
                    self.logger.debug("Optional " + requiresError)

    @requires(["motorDriver"], required=True)
    def turn(self, angle):
        """Turn around on the spot"""
        self.motorDriver.turn(angle)

    @requires(["motorDriver"], required=True)
    def moveForward(self, distance):
        """Move forward a certain distance"""
        self.motorDriver.moveForward(distance)


    @requires(["arm"])
    def setArmState(self, state):
        self.arm.setState(state)

    @requires(["pump"])
    def setPumpState(self, state):
        self.pump.setState(state)

    @requires(["vision", "visionMode"])
    def see(self, res = (800,600), stats = False):
        """See markers

        :param res: The resolution of the image to take with the camera
        :param stats: return additional statistics along with the
                      result, in a tuple"""
        return self.vision.see( res = res,
                                mode = self.visionMode,
                                stats = stats )

