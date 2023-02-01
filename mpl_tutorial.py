# Importing the class pyplot from matplotlib.
# as plt let's us write 'matplotlib.pyplot' simply as plt
# This line allows us to use the graphics/plotting capabilities
# of matplotlib.
import matplotlib.pyplot as plt


# Import numpy, but we can write np instead of numpy.
# This line allows us to use the math capabilities of numpy.
import numpy as np

# To draw a 2D plot we need points to plot. For every point there must be
# two bits of information, vertical and horizontal distances.

# The first bit of information is the horizontal distances.
# The np.arange(start, stop, interval) function creates
# a NumPy Array which is a list of sorted numbers starting at 'start'
# ending at 'stop' with any two consecutive numbers having a difference of interval. 
x = np.arange(0, 5, 0.1)

# This gives us the vertical distance for each correspoinding element of x.
# This line uses a sine function calculation on every of x.
y = np.sin(x)

# To plot these points we use the function 'plt.plot(x, y)' and 'plt.show()'.
plt.plot(x, y)
plt.title('Regular Plot')
plt.show()

# To plot multiple plots we simply use plot multiple times..

plt.title('Multiple Plots')
# We plot two curves with different colors and labels.
# Color is the color of the curve and labels are names of the curves.
plt.plot(x, y, label='Plot One', color='Red')
plt.plot(x, 2 * y, label='Plot Two', color='Blue')
# We can show a legend for our graph with the following.
plt.legend(loc='lower left')
plt.show()

# If instead of a continuous curve we wish to plot only the points
# we can use the 'plt.scatter(x, y)' function instead.
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()

# So far our plot is automatically fitting itself to the curve.
# We can also make some modifications to the axis lengths using the 'plt.aix([x_start, x_stop, y_start, y_stop])'
plt.plot(x,y)
plt.title('Regular Plot with A Different Fit')
plt.axis([0, 1, 0, 1])
plt.show()

# We can also change the title of the axis using 'plt.xlabel()' and 'plt.ylabel()'.
plt.plot(x,y)
plt.title('Regular Plot with Axis Labels')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
