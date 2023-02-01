# Import numpy, but we can write np instead of numpy.
# This line allows us to use the math capabilities of numpy.
import numpy as np

a = np.pi

# NumPy supports trignometric functions.
sine = np.sin(a)
cosine = np.cos(a)
tan = np.tan(a)

arcsine = np.arcsin(0)
arccos = np.arccos(0)

arctan = np.arctan(1/1)
arctan_2 = np.arctan2(1, 0)

# You can also convert angular units.
angle = 90
radians  = np.deg2rad(angle)
degree = np.rad2deg(radians)

# The power in NumPy comes from how it works with arrays.
array = [4, 3, 2, 1]

# We can define a NumPy array from a normal python list.
numpy_array = np.array(array)

# We also can sort them.

numpy_array_sorted = np.sort(numpy_array)


# We can also do operations on NumPy arrays! Such as
# Scalar Addition
scalar_addition = numpy_array + 2


print('Scalar Addition: ', scalar_addition)


# Scalar Multiplication
scalar_multiplication = 2 * numpy_array


print('Scalar Multiplication: ', scalar_multiplication)


# Element wise division.
array_division = numpy_array / numpy_array_sorted


print('Element Wise Division: ', array_division)

# Element wise multiplication.
array_multiplication = numpy_array * numpy_array_sorted


print('Element Wise Multiplication: ', array_multiplication)


# We also can create a NumPy array of even spaced values on
# a given interval using a single NumPy function, np.arange(start, stop, step).
start = 0
stop = 5
step = 0.5

domain = np.arange(start, stop, step)


print('Interval: ', domain)


# Lastly, we can even use our NumPy functions with NumPy arrays.
sine_of_interval = np.sin(domain)


print('Sine of Interval: ', sine_of_interval)
