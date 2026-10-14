import numpy as np

# array boradcasting

arr=np.array([1,2,3,4])
print(arr+10)

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([1,0,1])
print(matrix+vector)

print(np.sum(matrix))

print("Mean\n",np.mean(matrix))
# max , min , sum along row , col the same way
print("Standard deviation",np.std(matrix))


