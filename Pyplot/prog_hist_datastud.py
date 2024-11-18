#To plot a histogram with different formatiing and suitable title and labels

import numpy as np
import matplotlib.pyplot as plt

data_students=[1,11,21,31,41,51]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[10,1,0,33,6,8],
         facecolor='y',edgecolor="red")
plt.title("Histogram for Students data")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig("student.png")
plt.show()



















