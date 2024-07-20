#Joining two numpy arrays
import numpy as np
a = np.array([[1,2],[2,4]])
b = np.array([[7,8]])
c = np.concatenate((a,b), axis=0)
print(c)
d = np.concatenate((a,b.T), axis=1)
print(d)










