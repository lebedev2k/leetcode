from typing import List


def minimumOperations(nums: List[int]) -> int:
    s = set(nums)
    s.discard(0)
    return len(s)


def minimumOperations2(nums: List[int]) -> int:
    return len(set(nums) - {0})


assert(minimumOperations([1,0]) == 1)
assert(minimumOperations([1,5,0,3,5]) == 3)
assert minimumOperations([0]) == 0
assert minimumOperations([1,2,3,4,5]) == 5
assert minimumOperations([3,3,3,3]) == 1
