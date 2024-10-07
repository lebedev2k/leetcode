from typing import List

def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            diffrence = abs(nums[i] - nums[i-1])
            cnt += diffrence + 1
            nums[i] += diffrence + 1
    return cnt



assert minIncrementForUnique([1,2,2]) == 1
assert minIncrementForUnique([3,2,1,2,1,7]) == 6