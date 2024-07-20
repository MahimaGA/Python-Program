import numpy as np

import matplotlib.pyplot as plt

X =np.array([6,8,10,14,18])
Y = np.array([7,9,13,17.5,18])


print(X)
print(Y)

plt.figure()
plt.title('Pizza Price as a function of Pizza Diameter')
plt.xlabel('Pizza Diameter (Inches)')
plt.ylabel('Pizza Price (Dollars)')
axis = plt.axis([0, 25, 0 ,25])
np.polyfit(X,Y,1)
plt.grid(True)
plt.plot(X,Y, 'k')


plt.show()
