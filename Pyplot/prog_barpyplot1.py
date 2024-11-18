#Program to plot a Bar chart on the basis of popularity of Programming Languages

import numpy as np
import matplotlib.pyplot as plt
objects = ('DotNet', 'C++', 'Java', 'Python', 'C', 'CGI/PERL')
y_pos = np.arange(len(objects))
performance = [8,10,9,20,4,1]
plt.bar(y_pos, performance, align='center', color='blue')
plt.xticks(y_pos, objects) #set location and label
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()




