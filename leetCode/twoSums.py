"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""


# Two sum

def two_sum(array,target):
    dic ={}
    for i,n in enumerate(array):
        diff = target - n
        if diff in dic:
            return (dic[diff],i)
        else:
            dic[n] = i
    return dic

array1 = [2, 11, 8, 18, 9,7,15,4]
target1 = 9
print(two_sum(array1, target1))


def TwoSum(array,target):
    dict ={}
    for i,n in enumerate(array):
        diff = target - n
        if diff in dict:
            return (i,dict[diff])
        else:
            dict[n] = i


