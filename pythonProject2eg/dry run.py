import math

# Define the parameters for the milling operation
feed_rate = 100  # Feed rate in mm/min
spindle_speed = 10000  # Spindle speed in RPM
cutting_depth = 2  # Cutting depth in mm
tool_diameter = 6  # Tool diameter in mm
x_start = 0  # Starting X coordinate
y_start = 0  # Starting Y coordinate

# Define the milling path as a list of (x, y) coordinates
milling_path = [(10, 10), (20, 10), (20, 20), (10, 20), (10, 10)]

# Define the G-code commands for the milling operation
g_code = []
g_code.append('G90')  # Set absolute coordinates
g_code.append('G21')  # Set units to millimeters
g_code.append('G1 F{}'.format(feed_rate))  # Set feed rate
g_code.append('M3 S{}'.format(spindle_speed))  # Start spindle

# Move to the starting position and lower the tool
g_code.append('G0 X{} Y{}'.format(x_start, y_start))
g_code.append('G1 Z-{}'.format(cutting_depth))

# Mill the path
for x, y in milling_path:
    g_code.append('G1 X{} Y{}'.format(x, y))

# Lift the tool and stop the spindle
g_code.append('G1 Z0')
g_code.append('M5')

# Output the G-code to a file
with open('milling.nc', 'w') as f:
    for line in g_code:
        f.write(line + '\n')
