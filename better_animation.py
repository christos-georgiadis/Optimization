import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

def diagonal_5(x, y):
    x_part = np.log(np.exp(x) + np.exp(-x))
    y_part = np.log(np.exp(y) + np.exp(-y))
    return x_part + y_part


x = np.linspace(-20,20,150)
y = np.linspace(-20,20,150)
X, Y = np.meshgrid(x, y)
Z = diagonal_5(X, Y)

fig = plt.figure(figsize = (8,8))
ax = plt.axes(projection ='3d')
# plt.axis('off')
# ax.set_yticklabels([])
# ax.set_xticklabels([])
# ax.set_zticklabels([])

ax.plot_surface(X, Y, Z, cmap = 'viridis')


def rotate(angle):
     ax.view_init(azim=angle)

angle = 2
ani = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 360, angle), interval=50)
# ani.save('myfunction3.gif', writer=animation.PillowWriter(fps=10)) # when the white window appears, just wait. Do not close.
