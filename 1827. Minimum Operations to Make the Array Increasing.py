from typing import List

def minOperations(nums: list[int]) -> int:
    ops, i = 0, 0
    while i<len(nums)-1:
        if nums[i]>=nums[i+1]:
            ops += nums[i]-nums[i+1]+1
            nums[i+1] = nums[i] + 1
        i += 1
    return ops


assert minOperations([1,1,1]) == 3
assert minOperations([1,5,2,4,1]) == 14
assert minOperations([8]) == 0
