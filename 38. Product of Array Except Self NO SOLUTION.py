from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    from itertools import accumulate
    from operator import mul
    prefix = accumulate(nums, func=mul)
    
    


assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]