"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def num(x):
    for i in range(x):
        yield i

s=num(3)
print(s.__next__())
print(s.__next__())
#will work till i is 3

h="HariOm"
a=iter(h)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
