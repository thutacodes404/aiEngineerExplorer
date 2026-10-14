import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,3,5],[2,4,6],[1,3,7]])
print("original one \n",a)

# transpose
transpose=a.T
print("transpose \n",transpose)

print("addition",a+b)
print("Multiplication",a*b)


