import numpy as np

arr=np.array([1,2,4,5,6,7,8])

evens=arr[arr%2 == 0]
great=arr[arr>3]

print("Even",evens)
print(great)
arr[arr>3]=0
print("update",arr)