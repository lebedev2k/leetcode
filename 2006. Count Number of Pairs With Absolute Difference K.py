from typing import List
def countKDifference(nums: List[int], k: int) -> int:
    cnt = 0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if abs(nums[i]-nums[j])==k:
                cnt += 1
    return cnt
