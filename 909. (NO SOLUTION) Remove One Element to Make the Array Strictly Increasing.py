from typing import List

#свалился на тесте
#переделывал, но не сделано
def canBeIncreasing(nums: List[int]) -> bool:
    if len(nums) == 2:
        return nums[0] < nums[1]
    if len(nums) == 3:
        return nums[0] < nums[1] < nums[2]
    
    i = 0
    while i+2 < len(nums):
        if nums[i+1] > nums[i] > nums[i+2]:
    # deleted = False
    # i, j = 0, 1
    # while j < len(nums):
    #     if nums[i] >= nums[j]:
    #         if deleted:
    #             return False
    #         deleted = True
    #         if i > 0:
    #             if nums[i-1] < nums[j]:
    #                 i, j = j, j+1
    #         else:
    #             i, j = j, j+1
    #     else:
    #         i, j = j, j+1
            
    # return True

assert canBeIncreasing([105,924,32,968]) == True
assert canBeIncreasing([1,2,10,5,7]) == True
assert canBeIncreasing([2,3,1,2]) == False
assert canBeIncreasing([1,1,1]) == False
assert canBeIncreasing([10,5,7]) == True
assert canBeIncreasing([1, 2, 3, 4, 5]) == True
assert canBeIncreasing([1, 3, 2, 4, 5]) == True
assert canBeIncreasing([1, 3, 2, 5, 4]) == False
assert canBeIncreasing([1, 3, 2, 5, 6]) == True
