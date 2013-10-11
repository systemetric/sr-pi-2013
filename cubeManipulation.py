import time
import serial
from sr import *


def pump(state):
    """placeholder for the function to be created"""
    mbedComms = serial.Serial('/dev/ttyACM0', 115200)
    mbedComms.write('M2(state)')
    mbedComms.flush()
def pickUpCube():
    """Moves the arm down to the cube and sucks up the cube then raises the arm"""
    R.motors[2].target = 100
    time.sleep(2) #calibrating needed
    R.motors[2].target = 0
    pump(100)
    R.motors[2].target = -100
    time.sleep(2) #calibrating needed
    R.motors[2].target = 0
def dropCube():
    """Releases cube"""
    pump(0)
