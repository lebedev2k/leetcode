from typing import List

def maximumStrongPairXor(nums: List[int]) -> int:
    m = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]<=nums[j]:
                if nums[j]-nums[i]<=nums[i]:
                    x = nums[i]^nums[j]
                    if x>m:
                        m = x
    return m


assert maximumStrongPairXor([1,2,3,4,5]) == 7
assert maximumStrongPairXor([10,100]) == 0
assert maximumStrongPairXor([5,6,25,30]) == 7