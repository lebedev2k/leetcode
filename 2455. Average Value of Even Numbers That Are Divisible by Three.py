from typing import List
def averageValue(nums: List[int]) -> int:
    a = [v for v in nums if v%3 == 0]
    return int(sum(a)/len(a)) if len(a) > 0 else 0


assert averageValue([1,3,6,10,12,15]) == 9
assert averageValue([1,2,4,7,10]) == 0