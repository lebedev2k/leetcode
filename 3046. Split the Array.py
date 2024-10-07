from typing import List
from collections import Counter
def isPossibleToSplit(nums: List[int]) -> bool:
    c = Counter(nums)
    return max(c.values())>2