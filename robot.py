from sr import *
import time
import serial
import math
speed = 1
turncalibration = 1 """Use these two to calibrate movement"""
distancecalibration = 1


def PickAndPlinth():
    R = Robot()
    arena_list, robot_list, pedestal_list, cube_list = sortMarkers(R.See())
    MovementTarget = markerDistance(cube_list[0])
    moveForward(MovementTarget[1])
    if MovementTarget[0] < -0.2:
        turn(-90)
        moveForward(-MovementTarget[0])
    elif MovementTarget[0] > 0.2:
        turn(90)
        moveForward(MovementTarget[0])
    pickUpCube()
    PlinthTarget = markerDistance(pedestal_list[0])
    AdjustedMovement = (PlinthTarget[0]-MovementTarget[0], PlinthTarget[1]-MovementTarget[1])
    moveForward(AdjustedMovement[1])
    if AdjustedMovement[0]*AdjustedMovement[1] < 0:
        turn(-90)
        moveForward(AdjustedMovement[0])
    elif AdjustedMovement[0]*AdjustedMovement[1] > 0:
        turn(90)
        moveForward(AdjustedMovement[0])
    dropCube()

def moveForward(distance):
    """Moves the robot forwards a set amount of time
    (use negative distance for going backwards)
    input: distance"""
    if distance < 0: #if the time is negative, it becomes positive
        distance = distance*-1
        R.motors[0].target = -100
        R.motors[1].target = 100
    else:
        R.motors[0].target = 100
        R.motors[1].target = -100
    time.sleep(distance*distancecalibration)
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
    time.sleep(turncalibration*angle/90)
    R.motors[0].target = 0
    R.motors[1].target = 0
    
"""def moveToCubeBearing(Directions):
    turn(Directions.bearing)
    moveForward((Directions.distance)/speed)
    
    ...Go sit in a corner and think about what you did, whoever wrote this function ~Alistair"""
    
def markerDistance(marker):
    """Finds the relative forwards and sideways distance to a marker
    Input: marker
    Output: sideDist, forwardDist, totalDist"""
    forwardDist = 0
    sideDist = 0
    totalDist = 0
    p = marker.centre
    forwardDist = math.sin(math.rad(p.polar.rot_x))*p.polar.length
    sideDist = math.cos(math.rad(p.polar.rot_x))*p.polar.length
    totalDist = sideDist+forwardDist
    return sideDist, forwardDist, totalDist

def sortMarkers(markerList):
    """appends all the marker types to their own list
    input: markerList
    output: arena_list, robot_list, pedestal_list, cube_list"""
    arena_list = []
    robot_list = []
    pedestal_list = []
    cubes_list = []
    for marker in markerList:
        marker.sideDist, marker.forwardDist, marker.totalDist = markerDistance(marker)
        if marker.info.marker_type == MARKER_ARENA:
            arena_list.append(marker)
        if marker.info.marker_type == MARKER_ROBOT:
            robot_list.append(marker)
        if marker.info.marker_type == MARKER_PEDESTAL:
            pedestal_list.append(marker)
        if marker.info.marker_type == MARKER_TOKEN:
            cubes_list.append(marker)
    return arena_list, robot_list, pedestal_list, cube_list
def pump(state):
    """Changes the state of the pump from 0% to 100%"""
    mbedComms = serial.Serial('/dev/ttyACM0', 115200)
    mbedComms.write('pump(state)')
    mbedComms.flush()
def arm(state):
    """Changes the state of the arm from 0% to 100%"""
    mbedComms = serial.Serial('/dev/ttyACM0', 115200)
    mbedComms.write('arm(state)')
    mbedComms.flush()
def pickUpCube():
    """Moves the arm down to the cube and sucks up the cube then raises the arm"""
    arm(100)
    time.sleep(2) #calibrating needed
    arm(0)
    pump(100)
    arm(-100)
    time.sleep(2) #calibrating needed
    arm(0)
def dropCube():
    """Releases cube"""
    pump(0)
    
PickAndPlinth()
