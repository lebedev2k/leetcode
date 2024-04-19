from typing import List

def separateDigits(nums: List[int]) -> List[int]:
    from collections import deque
    res = []
    for n in nums:
        d = deque()
        while n>0:
            d.appendleft(n%10)
            n //= 10
        res.extend(d)
    return res

def separateDigits2(nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        res.extend([int(c) for c in str(n)])
    return res


def separateDigits3(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)-1,-1,-1):
        while nums[i]>0:
            res.append(nums[i]%10)
            nums[i] //= 10
    return res[::-1]

assert separateDigits3([13,25,83,77]) == [1,3,2,5,8,3,7,7]
assert separateDigits3([7,1,3,9]) == [7,1,3,9]
