

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield  a


# for val in fibonacci(12):
#     print(val)

# set operation
set1 = {x for x in range(0,40)}
set2 = {x for x in range(25,70)}
set3 = set((1, 2, 3, 3, 2, 1))
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}

# print(set1.intersection(set2))
print(set1.union(set2))
print(set1-set2)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

def fibo(n):
    a,b=0,1
    for _ in range(n+1):
        a,b = b,a+b     
        yield a

for val in fibo(12):
    print(val)
