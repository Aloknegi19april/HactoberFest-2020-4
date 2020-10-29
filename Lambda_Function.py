#Lambda Functions

from functools import *
# Simple Anonymous Function

f = lambda a : a+a
print(f(5))


#######

lst=[1,2,3,4,5,6,7,8,9,0]

even = list(filter(lambda a: a%2==0,lst))

print(even)

doubles = list(map(lambda n:n*2,even))

print(doubles)

avg = reduce(lambda a,b: a+b,doubles)
print(avg/10)
