# # say you have to exit the program after 15 sec
# import sys

# import time
# start = time.time()
# elapsed = 0
# # while True:
# #     print(time.time())
# #     time.sleep(1)
# #     elapsed = time.time() - start
# #     if elspsed>=int(15):
# #         sys.exit()
# #     print(elspsed)

# # for x in range(0,10000):
# #     print(x)

# while True:
#     elapsed = time.time() - start
#     print(elapsed)
#     time.sleep(1)
#     if elapsed>=15:
#         sys.exit()


# def myFunc(x=5):
#     print(x+1)

# myFunc()    # Prints 5
# myFunc(12)  # Prints 12

def myFunc(x=5, y=6):
    print(x + y)


myFunc()    # Prints 11
myFunc(12)  # Prints 18
myFunc(10, 10)  # Prints 20




# Lambda with Map() & Filter()
myList = [1, 4, 6, 7, 8, 11, 3, 4, 6]

newList = list(filter(lambda x:  x > 5, myList))
# newList is [6,7,8,11,6]
print(newList)

newList2 = list(map(lambda x: x+1, myList))
# newList 2 is [2,5,7,8,9,12,4,5,7]



import collections
from collections import Counter

c = Counter([1,1,1,3,4,5,6,7, 7])

print(c.most_common(1))  # returns [(1, 3)]
print(c.most_common(2))  # returns [(1, 3), (7, 2)]