# -*- coding: utf-8 -*-

import numpy as np
import math

# Degree to Radian
def D2R(x):
    """
    Degree to Radian Function
    Args
        Degree
    Return
        Radian
    """
    return (x/180)*math.pi

# Rotate Function
def RPY2XYZ(angles):
    """
    Perform a rotation matrix calculation based on the body Frame Rz, Ry, Rx with order of calculation respective of that
    Args
        Angles[0] = Roll: Angular position about the x-axis in radians.
        Angles[1] = Pitch: Angular position about the y-axis in radians.
        Angles[2] =Yaw: Angular position about the z-axis in radians.
    Return
        3x3
    """
    Rx = np.array([1,                   0,                    0, \
                   0, math.cos(angles[0]), -math.sin(angles[0]), \
                   0, math.sin(angles[0]),  math.cos(angles[0])  ]).reshape(3,3)
    
    Ry = np.array([math.cos(angles[1]), 0,  math.sin(angles[1]), \
                                     0, 1,                    0, \
                  -math.sin(angles[1]), 0,  math.cos(angles[1])  ]).reshape(3,3)
    
    Rz = np.array([math.cos(angles[2]), -math.sin(angles[2]), 0, \
                   math.sin(angles[2]),  math.cos(angles[2]), 0, \
                                     0,                    0, 1  ]).reshape(3,3)
    R = np.dot(Rz, np.dot(Ry,Rx))
    return R.transpose()

def plane(coordinates):
    # Defining the plane
    plane1 = np.array([
        [coordinates[0][0], coordinates[0][4], coordinates[0][5], coordinates[0][3], coordinates[0][0]],
        [coordinates[1][0], coordinates[1][4], coordinates[1][5], coordinates[1][3], coordinates[1][0]],
        [coordinates[2][0], coordinates[2][4], coordinates[2][5], coordinates[2][3], coordinates[2][0]]
    ])
    plane2 = np.array([
        [coordinates[0][2], coordinates[0][3], coordinates[0][5], coordinates[0][6], coordinates[0][2]],
        [coordinates[1][2], coordinates[1][3], coordinates[1][5], coordinates[1][6], coordinates[1][2]],
        [coordinates[2][2], coordinates[2][3], coordinates[2][5], coordinates[2][6], coordinates[2][2]]
    ])
    plane3 = np.array([
        [coordinates[0][0], coordinates[0][1], coordinates[0][2], coordinates[0][3], coordinates[0][0]],
        [coordinates[1][0], coordinates[1][1], coordinates[1][2], coordinates[1][3], coordinates[1][0]],
        [coordinates[2][0], coordinates[2][1], coordinates[2][2], coordinates[2][3], coordinates[2][0]]
    ])
    plane4 = np.array([
        [coordinates[0][0], coordinates[0][1], coordinates[0][7], coordinates[0][4], coordinates[0][0]],
        [coordinates[1][0], coordinates[1][1], coordinates[1][7], coordinates[1][4], coordinates[1][0]],
        [coordinates[2][0], coordinates[2][1], coordinates[2][7], coordinates[2][4], coordinates[2][0]]
    ])
    plane5 = np.array([
        [coordinates[0][1], coordinates[0][2], coordinates[0][6], coordinates[0][7], coordinates[0][1]],
        [coordinates[1][1], coordinates[1][2], coordinates[1][6], coordinates[1][7], coordinates[1][1]],
        [coordinates[2][1], coordinates[2][2], coordinates[2][6], coordinates[2][7], coordinates[2][1]]
    ])
    plane6 = np.array([
        [coordinates[0][4], coordinates[0][5], coordinates[0][6], coordinates[0][7], coordinates[0][4]],
        [coordinates[1][4], coordinates[1][5], coordinates[1][6], coordinates[1][7], coordinates[1][4]],
        [coordinates[2][4], coordinates[2][5], coordinates[2][6], coordinates[2][7], coordinates[2][4]]
    ])
    return plane1, plane2, plane3, plane4, plane5, plane6 

