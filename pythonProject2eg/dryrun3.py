# Define the size of the square
width = 50  # in millimeters
height = 50  # in millimeters

# Define the feed rate
feed_rate = 500  # in millimeters per minute

# Define the depth of cut
depth_of_cut = 2  # in millimeters

# Define the G-code file name
file_name = "square.nc"

# Open the G-code file for writing
with open(file_name, "w") as f:
    # Write the header
    f.write("G21\n")  # set units to millimeters
    f.write("G90\n")  # set absolute positioning
    f.write("G0 Z10\n")  # move the spindle up

    # Move to the starting position
    f.write("G0 X0 Y0\n")

    # Lower the spindle to the starting depth
    f.write("G1 Z{0} F{1}\n".format(-depth_of_cut, feed_rate))

    # Mill the square
    f.write("G1 X{0} Y0\n".format(width))
    f.write("G1 X{0} Y{1}\n".format(width, height))
    f.write("G1 X0 Y{0}\n".format(height))
    f.write("G1 X0 Y0\n")

    # Raise the spindle
    f.write("G0 Z10\n")

    # Write the footer
    f.write("M2\n")  # end the program
