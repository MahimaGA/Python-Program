#To plot two list elements using bar chart
import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y,label="Bars1")
plt.bar(x2,y2,label="Bars2")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Graph \n With multiline title')
plt.legend()
plt.show()



