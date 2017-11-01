from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

def derivative(list):
    return [list[i]-list[i-1] for i in range(1, len(list))]

data1 = np.loadtxt("2017_31_10_11_21_20_position.txt")
position_x =column(data1, 0)
position_y =column(data1, 1)
position_z =column(data1, 2)

speed_x = derivative(position_x)
speed_y = derivative(position_y)
speed_z = derivative(position_z)

acc_x = derivative(speed_x)
acc_y = derivative(speed_y)
acc_z = derivative(speed_z)

# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure1 = ax.plot(position_x, position_z, position_y, c='r')
figure2 = ax.plot(speed_x, speed_y, speed_z, c='b')
figure3 = ax.plot(acc_x, acc_y, acc_z, c='r')

plt.show()