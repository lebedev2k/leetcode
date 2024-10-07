from typing import List
from collections import Counter
def uniqueOccurrences(arr: List[int]) -> bool:
    c = Counter(arr)
    v = list(c.values())
    return len(v) == len(set(v))


assert uniqueOccurrences([1,2,2,1,1,3]) == True
assert uniqueOccurrences([1,2]) == False
assert uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])  == True