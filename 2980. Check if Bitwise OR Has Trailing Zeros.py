from typing import List

def hasTrailingZeros(nums: List[int]) -> bool:
    cnt = 0 
    for n in nums:
        if n%2 == 0:
            cnt += 1
            if cnt == 2:
                return True
    return False


assert hasTrailingZeros([1,2,3,4,5]) == True
assert hasTrailingZeros([2,4,8,16]) == True