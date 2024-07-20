#Copy function is used to create the copy of the existing array.

import numpy as np
x = np.array([1, 2, 3])
y = x
z = np.copy(x)
x[0] = 10
print(x)
print(y)
print(z)






