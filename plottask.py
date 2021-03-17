# Author: David Gilkeson

# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# Some marks will be given for making the plot look nice.

import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(0,4))
fx = x
gx = x * x
hx = x ** 3

# plot the functions and beautify the plot
plt.plot(x, fx, linestyle = "dotted", color = "green", marker = "o", ms = 8, label="f(x)=x")
plt.plot(x, gx, linestyle = "dashed",color = "cyan",marker = "o", ms = 8, label="g(x)=x^2")
plt.plot(x,hx, linestyle = "solid", color = "black", marker = "o", ms = 8, label="h(x)=x^3")

# show the plot with title, labels and legend
plt.title("Functions f(x)   g(x)    h(x)")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend(loc = "best")
plt.grid()
plt.show()

# References

# Matplotlib Getting Started. 2021. Matplotlib Getting Started. [ONLINE] Available at: https://www.w3schools.com/python/matplotlib_getting_started.asp. [Accessed 15 March 2021].

# Matplotlib Line. 2021. Matplotlib Line. [ONLINE] Available at: https://www.w3schools.com/python/matplotlib_line.asp. [Accessed 15 March 2021].

# Matplotlib Markers. 2021. Matplotlib Markers. [ONLINE] Available at: https://www.w3schools.com/python/matplotlib_markers.asp. [Accessed 15 March 2021].

# NumPy Getting Started. 2021. NumPy Getting Started. [ONLINE] Available at: https://www.w3schools.com/python/numpy_getting_started.asp. [Accessed 13 March 2021].

