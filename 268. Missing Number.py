from typing import List

def missingNumber(nums: List[int]) -> int:
    return list(set([i for i in range(len(nums)+1)]).difference(nums))[0]

def missingNumber2(nums: List[int]) -> int:
    nums.sort()
    origin = [i for i in range(len(nums)+1)]
    for i in range(len(nums)):
        if nums[i] != origin[i]:
            return origin[i]
    return len(nums)

def missingNumber3(nums: List[int]) -> int:
    h = {key: key for key in nums}
    origin = [i for i in range(len(nums)+1)]
    for i in origin:
        if i not in h:
            return i



assert missingNumber3([3,0,1]) == 2
assert missingNumber3([0,1]) == 2
assert missingNumber3([9,6,4,2,3,5,7,0,1]) == 8