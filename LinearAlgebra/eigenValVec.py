import numpy as np

# eigenvalues and vectors

# if A.v=l.v then v is eignevector and l is eignevalue

A=np.array([[1,2],[3,5]])

eigenval,eigenvect=np.linalg.eig(A)

print('eigen val \n',eigenval)
print('eigen vact \n',eigenvect)