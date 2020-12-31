# NumPy arrays are stored at one continuous place in memory unlike lists,
#  so processes can access and manipulate them very efficiently.
import time

# start_time = time.time()
# x = [x for x in range(45,10000000)]
# print(x[200099])
# print(time.time()-start_time)
# # 0.6203391551971436 sec

import numpy
start_time = time.time()
arr = numpy.array([x for x in range(45,10000000)])
print(arr[200099])
print(time.time()-start_time)
# 1.5408785343170166 sec