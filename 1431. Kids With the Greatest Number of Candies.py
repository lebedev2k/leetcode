from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    n = max(candies)
    return list(map(lambda x: x+extraCandies >= n, candies))


assert kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]   
assert kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
assert kidsWithCandies([12, 1, 12], 10) == [True, False, True]