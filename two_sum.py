# import


def two_sum(array,target):
    prevMap = {}
    for i,n in enumerate(array):
        diff = target - n
        if diff in prevMap:
            return (prevMap[diff],i)
        else:
            prevMap[n]=i
    
print(two_sum([0,2,4,6,7,9],target=9))