class Robot(object):
    """Systemetric enhancements to Student Robotics API"""

    def __init__(self, mode):
        self.mode = mode
        if not hasattr(self, "vision"):
            self.logger.warn("No `vision` object found: webcam code disabled")
        if not hasattr(self, "leftMotor"):
            self.logger.critical("No `leftMotor` object found")
            raise NotImplementedError("No `leftMotor` object found")
        if not hasattr(self, "rightMotor"):
            self.logger.critical("No `rightMotor` object found")
            raise NotImplementedError("No `rightMotor` object found")

    def see(self, res = (800,600), stats = False):
        if not hasattr(self, "vision"):
            raise RuntimeError("Camera not present")
        return self.vision.see( res = res,
                                mode = self.mode,
                                stats = stats )
