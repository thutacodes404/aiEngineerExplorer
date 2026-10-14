import numpy as np
dataset=np.random.randint(1,51,size=(5,5))
print("original ", dataset)

# filtering 
dataset[dataset>25]=0

print("modified one\n",dataset)
# calculate
print("Sum\n" ,np.sum(dataset))

print("Mean\n" ,np.mean(dataset))

print("StD\n" ,np.std(dataset))