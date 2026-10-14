import numpy as np

matrix=np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7],[2,4,6,8]])

print("Original one\n", matrix)
print("sum of the column\n",np.sum(matrix,axis=0))
print("sum of rows\n",np.sum(matrix,axis=1))

# finding min and max within a random array

# create a random number generator obj
random_arr=np.random.default_rng()

# create 2d array from it
D_arr=random_arr.random(size=(2,4))

print("random 2D array\n",D_arr)
print("max\n",D_arr.max())
print("min\n",D_arr.min())