import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.morphology import distance_transform_edt


x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
X, Y = np.meshgrid(x, y)


goal = np.array([40, 70])


obs = np.array([[10, 30], [40, 50], [70, 20]])

obs_dist = np.zeros_like(X)
for obstacle in obs:
    obs_dist = np.maximum(obs_dist, distance_transform_edt(np.sqrt((X-obstacle[0])**2 + (Y-obstacle[1])**2)))


alpha = 0.5 # conic potential constant
beta = 0.5 # quadratic potential constant
gamma = 0.5 # repulsive potential constant

# Define the potential function as a combination of conic and quadratic potential and repulsive potential
U = alpha * np.sqrt((X - goal[0])**2 + (Y - goal[1])**2)+beta * ((X - goal[0])**2 + (Y - goal[1])**2)+gamma * ((1/obs_dist - 1/10)**2)



# Calculate the gradient of the potential function
Ux, Uy = np.gradient(U)

# Display the gradient vector field using arrows
plt.figure(figsize=(10,10))
plt.quiver(X[::5,::5], Y[::5,::5], Ux[::5,::5], Uy[::5,::5])
plt.show()

#Ploting the  conic potential function
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
U_conic = alpha * np.sqrt((X - goal[0])**2 + (Y - goal[1])**2)
surf=ax.plot_surface(X, Y, U_conic,cmap=cm.jet)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('U Label')
ax.set_title("Conic potential function")
fig.colorbar(surf, shrink=0.5, aspect=5)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111, projection='3d')
U_conic=beta * ((X - goal[0])**2 + (Y - goal[1])**2)
surf=ax.plot_surface(X, Y, U_conic,cmap=cm.jet)
ax.contour(X, Y, U_conic)
ax.contour(X, Y, U_conic,20,   cmap="autumn_r", linestyles="solid", offset=-100)
ax.contour(X, Y, U_conic,20,   colors="k", linestyles="solid")
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('U Label')
ax.set_title("Quadratic potential function")