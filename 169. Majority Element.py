from typing import *
def majorityElement(nums: List[int]) -> int:
    from collections import Counter
    m = Counter(nums)
    n = len(nums)//2+1
    return max([key for key, value in m.items() if value>=n])


def majorityElement2(nums: List[int]) -> int:
    from collections import defaultdict
    m = defaultdict(int)
    res = [] 
    n = len(nums)//2+1
    for num in nums:
        m[num] += 1
        if m[num]>=n:
            res.append(num)
    return max(res)



assert majorityElement2([3,2,3]) == 3
assert majorityElement2([2,2,1,1,1,2,2]) == 2
