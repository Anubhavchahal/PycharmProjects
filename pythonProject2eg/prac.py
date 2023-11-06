import math

# Define the parameters
center_x = 0
center_y = 0
radius = 10
num_points = 50
feed_rate = 200 # in mm/min

# Generate the path
path = []
for i in range(num_points):
    angle = 2 * math.pi * i / num_points
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    path.append((x, y))

# Output the G-code commands
print("G21")  # Metric system
print("G90")  # Absolute positioning
print("F{}".format(feed_rate))
for point in path:
    print("G01 X{:.3f} Y{:.3f}".format(point[0], point[1]))
print("G00 X{:.3f} Y{:.3f}".format(center_x, center_y))  # Return to the center

# Plot the path
x_vals = [p[0] for p in path]
y_vals = [p[1] for p in path]
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals)
ax.set_title("Circular Path")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()