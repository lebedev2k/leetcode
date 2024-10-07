from typing import List
from collections import Counter

def repeatedNTimes(nums: List[int]) -> int:
    return Counter(nums).most_common(1)[0][0]


assert repeatedNTimes([1, 2, 3, 3]) == 3
assert repeatedNTimes([2,1,2,5,3,2])  ==  2
assert repeatedNTimes([5,1,5,2,5,3,5,4])  ==  5