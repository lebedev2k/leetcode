from typing import List
def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
    # s = 0
    # for i in range(len(nums)):
    #     if bin(i).count('1') == k:
    #         s += nums[i]
    return sum(nums[i] for i in range(len(nums)) if bin(i).count('1') == k)

assert sumIndicesWithKSetBits([5,10,1,5,2], 1) == 13