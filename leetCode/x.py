nums = [x for x in range(45,1500)]
nums.pop(122)
print(nums)
n = None
smallest = nums[0]
largest = nums[-1]
ran = [x for x in range(smallest,largest+1)]
for n in ran:
    if n not in nums:
        print(n)
        