import numpy as np

A = np.array([[1,2],[3,4]])
b = np.array([1,2])
print(A)
print(b)

x = np.linalg.inv(A).dot(b)# In matlab, get warning if you use inv(A)
print(x)
print(np.linalg.solve(A,b)) #always use solve(), never use inverse mathod