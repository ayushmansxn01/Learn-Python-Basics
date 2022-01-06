#-----------MAP-------
#map to convert one data type to other eg: convvert list of string to list of integer, map returns pointer and
# therefore it has to be converted to list
number=["2","3","5","7"]
number=list(map(int,number))
print(number)
print(type(number))

#---------------Filter---------------
list1=[1,2,3,4,5]
def suma(a):
    return a>2
c=list(filter(suma,list1))
print(c)

#--------------Reduce---------
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)
print(num)