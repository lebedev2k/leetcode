from typing import List
from collections import Counter

def findLucky(arr: List[int]) -> int:
    c = Counter(arr)
    a = sorted(filter(lambda item: item[0] == item[1], c.items()))
    return a[-1][0] if a else -1


assert findLucky([2,2,3,4]) == 2
assert findLucky([1,2,2,3,3,3]) == 3
assert findLucky([2,2,2,3,3]) == -1
