from typing import List
def canBeEqual(target: List[int], arr: List[int]) -> bool:
    target.sort()
    arr.sort()
    return target == arr

assert canBeEqual([1,2,3,4], [2,4,1,3]) == True