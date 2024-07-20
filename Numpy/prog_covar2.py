#To calculate the covariance matrix and covariance value
#from the computed covariance matrix

import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print(x)
y = np.array([9,8,7,6,5,4,3,2,1])
print(y)
cov_mat= np.cov(x,y)
print("Covariance matrix is: ")
print(cov_mat)
cov_value =np.cov(x,y)[0,1]
print("Covariance value is:",cov_value)


