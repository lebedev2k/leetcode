from typing import List

def minDifference(nums: List[int]) -> int:
    if len(nums)<5: return 0
    nums.sort()
    n = len(nums)
    return min([nums[n-4+i] - nums[i] for i in range(4)])


assert minDifference([1,5,0,10,14]) == 1
assert minDifference([5,3,2,4]) == 0
assert minDifference([3,100,20]) == 0

