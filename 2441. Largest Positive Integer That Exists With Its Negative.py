from typing import List

def findMaxK2(nums: List[int]) -> int:
    nums.sort(reverse=True)
    d = {}
    for n in nums:
        if n > 0:
            if not n in d:
                d[n] = None
        else:
            if -n in d:
                d[-n] = 1
    r = sorted(filter(lambda x: x[1] is not None, d.items()), reverse=True)
    return -1 if not r else r[0][0]


def findMaxK(nums: List[int]) -> int:
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] == -nums[j]:
            return nums[j]
        if -nums[i]>nums[j]:
            i+=1
        else:
            j-=1
    return -1
                                
    
assert findMaxK([2, -2, -3, 3]) == 3
assert findMaxK([-1,10,6,7,-7,1]) == 7
assert findMaxK([-10,8,6,7,-2,-3]) == -1
assert findMaxK([1,2,3,4,5]) == -1