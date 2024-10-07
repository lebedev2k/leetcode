from functools import reduce
import operator
from typing import List
from itertools import combinations, accumulate


def subsetXORSum(nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(1, n+1):
        for subset in combinations(nums, i):
            ans += reduce(lambda x, y: x ^ y, subset)
    return ans


assert subsetXORSum([1,3]) == 6
assert subsetXORSum([5,1,6]) == 28
assert subsetXORSum([3,4,5,6,7,8]) == 480

