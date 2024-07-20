import numpy as np
a = np.array([1000,1200,1600])
b = np.array([130,110,120])
print(np.cov(a,b,bias=True)[0,1])
