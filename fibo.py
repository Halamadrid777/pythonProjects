from algorithms.sort import bubble_sort
import random
from algorithms.sort import bogo_sort

count = 0
random_numbers = []
while count<10000:
    x = random.randint(0,100000)
    random_numbers.append(x)
    count+=1

print(sorted(random_numbers))
print(bogo_sort(random_numbers))