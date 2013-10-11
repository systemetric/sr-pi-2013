import math
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

from sr import *
R = Robot()
print(sortMarkers(R.See))