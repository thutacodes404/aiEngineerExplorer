import numpy as np

arr=np.array([1,2,3,4,])
print(arr)

zeros=np.zeros((3,3))
ones=np.ones((2,4))

range_arr=np.arange(2,11,2)

line_space=np.linspace(0,10,5)


print(line_space)
print(zeros)
print(ones)
print(range_arr)



# manipulating arrays
ar1=np.array([1,2,3,4,5,6,7,8])
expended=ar1[:,np.newaxis]
reshape=ar1.reshape(4,2)
print(reshape)
print(expended)


# basic operation

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)
print(a/b)

ar2=np.array([4,16,25])

print(np.sqrt(ar2))
print(np.sum(ar2))
print(np.mean(ar2))
print(np.max(ar2))

# slice shape 

ar3=np.array([10,20,30,40,50,60])

print(ar3[2])
print(ar3[-1])

print(ar3[1:4])
print(ar3[3:])

print(ar3.reshape(2,3))