import vision
import os, glob

class VisionShim(vision.Vision):
    """Systemetric shim for the vision code from SR2013
    """
    def __init__(self, device='/dev/video0', libpath=None):
        """Constructor

    
        :param device: the camera device
        :param libpath: the path to libkoki.so or None
        :raises: RuntimeError -- when camera not found
        """

        if not os.path.exists(device):
            raise RuntimeError("Camera not found")

        # Find libsric.so:
        if libpath is None and  "LD_LIBRARY_PATH" in os.environ:
            for d in os.environ["LD_LIBRARY_PATH"].split(":"):
                l = glob.glob( "%s/libkoki.so*" % os.path.abspath( d ) )

                if len(l):
                    libpath = os.path.abspath(d)
                    break

        if libpath is None:
            raise RuntimeError("libkoki not found")
        super(VisionShim, self).__init__(device, libpath)


