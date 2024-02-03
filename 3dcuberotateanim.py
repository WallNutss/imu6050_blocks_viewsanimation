import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import serial

# Importing rotation matrix
from lib.rotation import RPY2XYZ, D2R, plane

# Importing custom own plotting
from lib.plotting import insideAnimation, outsideAnimation, smallDetails

# Opening Serial Communication first to ESP32
comm = serial.Serial('COM3', baudrate=57600)

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

state_display = ax.text2D(0.07, 1.0, "" ,color='green', transform=ax.transAxes)
error_display = ax.text2D(0.07, 0.95, "" ,color='red', transform=ax.transAxes)

#If you want the block one
one   = np.array([0.2, 0.2, 0])
two   = np.array([0.2, 1.2, 0])
three = np.array([0.8, 1.2, 0])
four  = np.array([0.8, 0.2, 0])
five  = np.array([0.2, 0.2, 0.6])
six   = np.array([0.8, 0.2, 0.6])
seven = np.array([0.8, 1.2, 0.6])
eight = np.array([0.2, 1.2, 0.6])

# Define the coordinates for the cubic shape, its the x,y, and z of the coordinate
x = np.array([one[0], two[0], three[0], four[0], five[0], six[0], seven[0], eight[0]])
y = np.array([one[1], two[1], three[1], four[1], five[1], six[1], seven[1], eight[1]])
z = np.array([one[2], two[2], three[2], four[2], five[2], six[2], seven[2], eight[2]])

# Rotating 0 Degree from x-axis
phi = D2R(0)
theta = D2R(0)
psi = D2R(0)

angles = np.array([phi, theta, psi])
Rotating = RPY2XYZ(angles)

new_x = np.array([])
new_y = np.array([])
new_z = np.array([])

# Center of Mass
com = np.array([x.mean(),y.mean(),z.mean()])
ax.plot(com[0], com[1], com[2], 'ro')

for i in range(x.shape[0]):
    # Taking in the first coordinates from the d,e,and f
    raw = np.array([x[i]-com[0],y[i]-com[1],z[i]-com[2]]).reshape(3,1)
    # Times in with rotation matrix
    ans = np.dot(Rotating,raw)
    new_x = np.append(new_x, ans[0]+com[0])
    new_y = np.append(new_y, ans[1]+com[1])
    new_z = np.append(new_z, ans[2]+com[2])

# Plotting the cube
coordinates = np.array([new_x, new_y, new_z])
line1, line2, line3, line4, line5, line6 = outsideAnimation(plane(coordinates),ax)

# Set axis labels, plot limits, and reverse axis
smallDetails(ax)

def update_point(n):

    try:
        arduinoData = comm.readline().decode('ascii').split(';')
        phi, theta, psi = arduinoData
        phi, theta, psi = float(phi), float(theta), float(psi)

        angles[0], angles[1], angles[2]  = D2R(phi), D2R(theta), D2R(psi)
        Rotate = RPY2XYZ(angles)
        error_display.set_text(rf"")
    except:
        phi, theta, psi = 0.0, 0.0, 0.0

        angles[0], angles[1], angles[2]  = D2R(phi), D2R(theta), D2R(psi)
        Rotate = RPY2XYZ(angles)
        error_display.set_text(rf"Please wait, there's something wrong with the data")
    
    
    com = np.array([x.mean(),y.mean(),z.mean()])

    new_x = np.array([])
    new_y = np.array([])
    new_z = np.array([])

    for i in range(x.shape[0]):
        raw = np.array([x[i]-com[0],y[i]-com[1],z[i]-com[2]]).reshape(3,1)
        ans = np.dot(Rotate,raw)

        new_x = np.append(new_x, ans[0]+com[0])
        new_y = np.append(new_y, ans[1]+com[1])
        new_z = np.append(new_z, ans[2]+com[2])
        
    coordinates = np.array([new_x, new_y, new_z])
    plane1, plane2, plane3, plane4, plane5, plane6 = plane(coordinates)

    insideAnimation(line1, line2, line3, line4, line5, line6, plane1, plane2, plane3, plane4, plane5, plane6)

    state_display.set_text(rf'IMU MPU6050 Rotation'
                           '\n'
                           rf'$\phi$:{round(phi,2)}$^\circ$  $\theta$:{round(theta,2)}$^\circ$  $\psi$:{round(psi,2)}$^\circ$')

    return line1, line2, line3, line4, line5, line6

ani = animation.FuncAnimation(fig, update_point, interval=10)

# Show the plot

plt.show()

plt.close()