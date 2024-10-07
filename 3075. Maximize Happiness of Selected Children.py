from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    return sum([max(val-i,0) for i,val in enumerate(happiness[:k])])


assert maximumHappinessSum([1,2,3], 2) == 4
assert maximumHappinessSum([1,1,1,1], 2) == 1
assert maximumHappinessSum([2,3,4,5], 1) == 5
assert maximumHappinessSum([2,3,4,5], 3) == 9

        