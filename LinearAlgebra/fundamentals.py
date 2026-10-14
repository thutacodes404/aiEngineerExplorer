# element wise operations

import numpy as np

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

# print("Addition\n",A+B)
# print("Subtraction\n",A-B)

C=2*A

mulres=np.dot(A,B)
# print("Multiplication\n",mulres)

I=np.eye(3)
# print("Identity martrix\n",I)

zeros=np.zeros((3,3))
# print("Zero Matrix\n",zeros)

diagonal=np.diag([1,2,3])
print('Diagonal Matrix\n',diagonal)