import numpy as np

A=np.array([[1,2],[3,4]])

B=np.array([[5,6],[7,8]])

print('Addition\n',A+B)
print("Subtraction\n",B-A)
print("Scalar Multiplication\n",3*A)

result=np.dot(A,B)
print('Matrix Mul \n',result)

# identity metrix
I=np.eye(5)
print('identity matrix\n',I)
# zeros
Z=np.zeros((2,3))
print('zero matrix\n',Z)

D=np.diag([1,2,3])
print('Diagonal Matrix \n',D)
