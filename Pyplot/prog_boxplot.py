#To plot a simple boxplot

import matplotlib.pyplot as plt

list1 = [43,76,34,63,56,82,87,55,64,87,95,23,14,65,67,25,23,85]
list2 = [34,45,34,23,43,76,26,18,24,74,23,56,23,23,34,56,32,23]
data = [list1,list2]   #Passing nested lists (lists inside a list)

plt.boxplot(data)
plt.show()






