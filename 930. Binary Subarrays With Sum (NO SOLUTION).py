from typing import List

#fail on test with time limit
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    counter = 0 
    left = right = 0
    n = len(nums)
    summ = nums[left]
    while left<n:
        if summ == goal:
            counter += 1
        
        right += 1
        if right<n:
            summ += nums[right]
        else:
            left +=1
            right = left
            if left<n:
                summ = nums[left]
        
    return counter


assert numSubarraysWithSum([1,0,1,0,1], 2) == 4
assert numSubarraysWithSum([0,0,0,0,0], 0) == 15