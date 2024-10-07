from typing import List
from itertools import accumulate
def rangeSum(nums: List[int], n: int, left: int, right: int) -> int:
    a = list(accumulate(nums, initial=0))
    new_array = []
    for i in range(1,len(a)):
        for j in range(i, len(a)):
            new_array.append(a[j]-a[i-1])
    new_array.sort()
    return sum(new_array[left-1:right])%((10**9)+7)

assert rangeSum([1,2,3,4], 4, 1,5) == 13
assert rangeSum([1,2,3,4], 4, 3,4) == 6
assert rangeSum([1,2,3,4], 4, 1,10) == 50
