from itertools import *

#solution 1
def removeDuplicates(nums: list[int]) -> int:
    from collections import Counter
    c = Counter(nums)
    for i, item in enumerate(c.keys()):
        nums[i] = item
    return len(c)

#solution 2
def removeDuplicates2(nums: list[int]) -> int:
    current_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[current_index]:
            current_index += 1
            nums[current_index] = nums[i]
    return current_index+1

nums = [1,1,2]    
# assert(removeDuplicates2(nums)==2)
print(removeDuplicates2(nums))
print(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
assert(removeDuplicates2(nums)==5)
print(nums)

