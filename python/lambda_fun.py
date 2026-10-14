# lambda functions
from functools import reduce


add= lambda x,y : x+y

lists=[1,2,3,4,5]

square=map(lambda x: x**2,lists)

evenlist=filter(lambda x: x%2==0,lists)

product= reduce(lambda x,y : x*y , lists)


print(list(square))
print(product)
print(list(evenlist))
print (add(3,5))