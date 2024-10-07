from typing import List

def largestAltitude(gain: List[int]) -> int:
    from itertools import accumulate
    return max(accumulate(gain, initial=0))