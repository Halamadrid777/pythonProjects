

# a_z = []
# A_Z = []
# for alpha in range(97, 123):
#     a_z.append(chr(alpha))
#     A_Z.append(chr(alpha).upper())


# print(a_z)
# print(A_Z)

# for i in range(0, len(a_z)):
#     x = set(map(str(i), a_z[i]))

# print(x.__dict__)


def isAOne(x):
    return x == 1

nums = [1,1,6,7,8,0,1,1]

newList = list(filter(isAOne,nums))
print(newList)
# newList is [1,1,1,1]