from itertools import accumulate
from typing import List

#fail on Time Limit Exceeded

def subarraysDivByK(nums: List[int], k: int) -> int:
    cnt = 0
    p_sum = list(accumulate(nums, initial=0))
    for i in range(0, len(p_sum)):
        for j in range(i+1, len(p_sum)):
            l_sum  =  p_sum[j]  -  (p_sum[i])
            if l_sum % k  == 0:
                cnt  +=  1
    return cnt


assert subarraysDivByK([0] * 30000, 10000) == 0 #Time Limit Exceeded
assert subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
assert subarraysDivByK([5], 9) == 0
