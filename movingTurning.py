from sr import *
import time
R = Robot()
speed = 0
def moveForward(time):
    """Moves the robot forwards a set amount of time
    (use negative speed for going backwards)
    input: seconds, speed(%)"""
    if time < 0: #if the time is negative, it becomes positive
        time = time*-1
    R.motors[0].target = 100
    R.motors[1].target = -100
    time.sleep(time)
    R.motors[0].target = 0
    R.motors[1].target = 0
    
def turn(angle):
    """Turns the robots a set angle assuming it takes 1s to turn 90
    input: angle"""
    if angle == -180:
        angle = 180
    if angle < 0:
        angle = (angle*-1)+180
    while angle > 359:
        angle = angle-360
    R.motors[0].target = 100
    R.motors[1].target = 100
    time.sleep(angle/90)
    R.motors[0].target = 0
    R.motors[1].target = 0
    
def moveToCubeBearing(Directions):
    turn(Directions.bearing)
    moveForward((Directions.distance)/speed)
