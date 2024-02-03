import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


def insideAnimation(line1, line2, line3, line4, line5, line6, plane1, plane2, plane3, plane4, plane5, plane6):
    line1.set_data(plane1[0],plane1[1])
    line1.set_3d_properties(plane1[2])

    line2.set_data(plane2[0],plane2[1])
    line2.set_3d_properties(plane2[2])

    line3.set_data(plane3[0],plane3[1])
    line3.set_3d_properties(plane3[2])

    line4.set_data(plane4[0],plane4[1])
    line4.set_3d_properties(plane4[2])

    line5.set_data(plane5[0],plane5[1])
    line5.set_3d_properties(plane5[2])

    line6.set_data(plane6[0],plane6[1])
    line6.set_3d_properties(plane6[2])


def outsideAnimation(data, ax):
    line1, = ax.plot(data[0][0], data[0][1], data[0][2], linestyle='dashed')
    line2, = ax.plot(data[1][0], data[1][1], data[1][2], linestyle='dashed')
    line3, = ax.plot(data[2][0], data[2][1], data[2][2], linestyle='dashed')
    line4, = ax.plot(data[3][0], data[3][1], data[3][2], linestyle='dashed')
    line5, = ax.plot(data[4][0], data[4][1], data[4][2], linestyle='dashed')
    line6, = ax.plot(data[5][0], data[5][1], data[5][2], linestyle='dashed')

    return line1, line2, line3, line4, line5, line6

def smallDetails(ax):
    ax.set_xlabel('X', fontweight="bold")
    ax.set_ylabel('Y', fontweight="bold")
    ax.set_zlabel('Z', fontweight="bold")

    # Set plot limits
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_zlim(-0.5, 1.5)

    ax.grid(False)

    # Reverse
    ax.invert_xaxis()
    ax.invert_yaxis()

    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.zaxis.set_major_locator(MultipleLocator(0.5))