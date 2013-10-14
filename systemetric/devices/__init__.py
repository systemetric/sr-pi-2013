"""Devices that form part of a SR-less robot

These variants of the devices are used when we strip out the SR robot
of any SR specific parts and use our own bits and pieces instead.
Use these in the Raspberry Pi robots.
"""

from mbed import Mbed, MbedTimeout
from motor import MotorMbed
