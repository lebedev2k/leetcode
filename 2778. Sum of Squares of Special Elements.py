from typing import List
def sumOfSquares(nums: List[int]) -> int:
    res = 0
    n = len(nums)
    for i in range(n):
        if n%(i+1)==0: res += nums[i] * nums[i]
   
    return res


assert sumOfSquares([1,2,3,4]) == 21
assert sumOfSquares([2,7,1,19,18,3]) == 63
