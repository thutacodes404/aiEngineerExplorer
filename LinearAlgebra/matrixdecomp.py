import numpy as np

# singular value decomposition(SVD)
A=np.array([[1,2],[3,4]])
U,S,Vt=np.linalg.svd(A)

print('U\n',U)
print('singular value\n',S)
print('V transport value\n',Vt)

