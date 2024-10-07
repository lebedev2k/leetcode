#NO SOLUTION
from typing import List
def maxDistance(arrays: List[List[int]]) -> int:
    arrays.sort()
    print(arrays)


assert maxDistance([[1,2,3],[4,5],[1,2,3]]) == 4
assert maxDistance([[1],[1]]) == 0