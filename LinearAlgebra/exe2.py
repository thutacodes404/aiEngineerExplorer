import numpy as np

# matrix and vectr multiplication

M=np.array([[1,2,3],[5,6,7]])
V=np.array([1,0,-1])

res=np.dot(M,V)
print('V\n',V)
print('M\n',M)
print('result\n',res)