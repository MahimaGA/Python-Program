#To plot a simple bar chart
import matplotlib.pyplot as plt;

# Variables for the bar chart
y_axis = [20,50,30]
x_axis = range(len(y_axis))
plt.bar(x_axis, y_axis, width=.5, color='orange')
plt.show()




