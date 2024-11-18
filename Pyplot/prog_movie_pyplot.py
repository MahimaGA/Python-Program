#Program to plot a bar chart showing the choice of
#favorite movie among the people

import numpy as np
import matplotlib.pyplot as plt
objects = ('Comedy', 'Action', 'Romance', 'Drama', 'SciFi')
y_pos = np.arange(len(objects))
Types = (4,5,6,1,4)
plt.bar(y_pos, Types, align='center', color='blue')
plt.xticks(y_pos, objects)      #set location and label
plt.ylabel('People')
plt.title('Favourite Type of Movie')
plt.show()


