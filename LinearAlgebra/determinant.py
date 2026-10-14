import numpy as np

A=np.array([[2,3],[1,2]])

determin=np.linalg.det(A)
print(determin)

inverse=np.linalg.inv(A)
print('inverse\n',inverse)
