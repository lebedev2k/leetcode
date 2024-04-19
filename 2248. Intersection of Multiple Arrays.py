# 2248. Intersection of Multiple Arrays
from typing import List

def intersection2(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    from collections import defaultdict
    counter = defaultdict(int)
    for row in nums:
        for elem in row:
            counter[elem] += 1
    return [item[0] for item in counter.items() if item[1]==n]

def intersection(nums: List[List[int]]) -> List[int]:
    res = set(nums[0])
    for row in nums:
        res = set(row) & res
    return sorted(list(res))


assert intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3,4]
assert intersection([[1,2,3],[4,5,6]]) == []