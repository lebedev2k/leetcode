from typing import List
def minSwaps(nums: List[int]) -> int:
    n = sum(nums)
    length = len(nums)
    n2 = n1 * 2
    nums = nums*2
    start, end = 0, n
    min_swaps = n2
    while end < n2:
        min_swaps = min(min_swaps, nums[start:end].count(0))
        start += 1
        end += 1
    return min_swaps


assert minSwaps([0,1,0,1,1,0,0]) == 1
assert minSwaps([0,1,1,1,0,0,1,1,0]) == 2
assert minSwaps([1,1,0,0,1]) == 0
