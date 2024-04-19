from typing import List

def maxOperations(nums: List[int]) -> int:
    score = nums[0]+nums[1]
    counter = 1
    i = 2
    n = len(nums)
    while i<n-1 and nums[i]+nums[i+1]==score:
        i += 2
        counter += 1
    return counter


assert maxOperations([3,2,1,4,5]) == 2
assert maxOperations([3,2,6,1,4]) == 1
assert maxOperations([1,1,1,1,1,1]) == 3