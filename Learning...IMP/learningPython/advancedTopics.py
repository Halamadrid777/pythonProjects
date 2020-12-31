# def rev_str(my_str):
#     length = len(my_str)
#     for i in range(length - 1, -1, -1):
#         yield my_str[i]


# # For loop to reverse the string
# for char in rev_str("hello"):
#     print(char)


# generate even
# even = [x for x in range(0,101,2) ]
# odd = [x for x in range(1,101,2) ]
# print(even)
# print(odd)

# for x in range(0,100):
#     if x%2 != 0:
#         print(x)

# def make_class(x):
#     class Dog():
#         def __init__(self,name):
#             self.name = name

#         def print_class(self):
#             print(x)
#     return Dog
# cls = make_class(10)
# d = cls("tim")
# print(d.name)
# d.print_class()


# for i in range(10):
#     def show():
#         print(i*2)
    
#     show()


# for i in range(10):
#     print(i*2)


def  func(x):
    if x ==1:
        def rv():
            print("X is equla to 1")
    else:
        def rv():
            print("X is not equal to 1")
    
    return rv

my_func = func(21)
my_func()
import inspect
import math
from math import factorial, sqrt
print(inspect.getsource(my_func))
print(inspect.getsource(math.sqrt))