from typing import List

def findFinalValue(nums: List[int], original: int) -> int:
    a = {n: n for n in nums}
    
    if original in a:
        prev_original = original
        while original in a:
            prev_original = original
            original *= 2
    else:
        return original    
    return prev_original*2
    


assert findFinalValue([5,3,6,1,12], 3) == 24
assert findFinalValue([2,7,9], 4) == 4