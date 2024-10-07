from typing import List
def longestSubarray(nums: List[int]) -> int:
    k = max(nums)
    max_subarray_len = 0
    cur_len = 0
    for n in nums:
        if n == k:
            cur_len += 1
            max_subarray_len = max(cur_len,max_subarray_len)
        else:
            cur_len = 0
    return max_subarray_len


assert longestSubarray([1,2,3,3,2,2]) == 2
assert longestSubarray([1,2,3,4]) == 1