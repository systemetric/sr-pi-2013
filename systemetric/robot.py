import logging

def requires(thing, required=False):
    def do_decorate(func):
        def decorated(self, *args, **kwargs):
            if not hasattr(self, thing):
                raise RuntimeError("`{}` object (required by `{c}.{f}`) "
                                   "not initialised in {c}"
                                   .format(thing,
                                           f=func.__name__,
                                           c=self.__class__.__name__))
            return func(self, *args, **kwargs)
        decorated._requires_data = (thing, required)
        return decorated
    return do_decorate

class Robot(object):
    """Systemetric enhancements to Student Robotics API"""

    def __init__(self, mode):
        self.mode = mode
        className = self.__class__.__name__

        self.logger = logging.getLogger(className)

        # check requires
        failedRequirements = set()
        for name in dir(self):
            try:
                method = getattr(self, name)
            except AttributeError:
                continue
            if not hasattr(method, "_requires_data"):
                continue
            thing, required = method._requires_data
            if not hasattr(self, thing):
                if required:
                    failedRequirements.add(thing)
                else:
                    self.logger.debug(
                            "`{}` optional object (required by `{c}.{f}`) "
                            "not initialised in {c}"
                            .format(thing, f=name, c=className))
        if failedRequirements:
            raise NotImplementedError(
                    "These required objects are not initialised in {c}: {}"
                    .format(', '.join(failedRequirements), c=className))

    @requires("motorDriver", required=True)
    def turn(self, angle):
        self.motorDriver.turn(angle)

    @requires("motorDriver", required=True)
    def moveForward(self, distance):
        self.motorDriver.moveForward(distance)


    @requires("arm")
    def setArmState(self, state):
        self.arm.setState(state)

    @requires("pump")
    def setPumpState(self, state):
        self.pump.setState(state)

    @requires("vision")
    def see(self, res = (800,600), stats = False):
        return self.vision.see( res = res,
                                mode = self.mode,
                                stats = stats )

