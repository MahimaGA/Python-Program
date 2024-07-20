#Program to plot a quadratic equation using dashed Line Chart
# 1 - 0.5*x**2

import matplotlib.pyplot as plt
import numpy as np
xvals = np.arange(-2, 1, 0.01)   #Grid of 0.01 spacing from -2 to 1
newyvals = 1 - 0.5 * xvals**2    #Evaluate quadratic approximation on xvals
plt.plot(xvals, newyvals, 'b--') #Create line plot with blue dashed line
plt.title('Example plots')       #Creates heading Text
plt.xlabel('Input')              #Creates Text along x-axis
plt.ylabel('Function values')    #Creates text along y-axis
plt.show()              # Show the figure (remove the previous instance)


