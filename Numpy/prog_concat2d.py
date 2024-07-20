#Concatenate two 2D arrays using single array

import numpy as np
A = np.array([[7,5],[1,6]])
# concatenate along the first axis
print(np.concatenate([A, A]))
#concatenate along the second axis (zero-indexed)
print(np.concatenate([A, A], axis=1))
x = np.array([1, 2])
# vertically stack the arrays
print(np.vstack([x, A]))   
# horizontally stack the arrays
y = np.array([[99],[99]])
print(np.hstack([A, y]))











