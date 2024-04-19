from typing import List

def prefixesDivBy5(nums: List[int]) -> List[bool]:
    num = ''
    res = []
    for n in nums:
        num += str(n)
        if int(num,2)%5 == 0:
            res.append(True)
        else:
            res.append(False)
    
    return res


def prefixesDivBy52(nums: List[int]) -> List[bool]:
    num = 0
    res = []
    for n in nums:
        num = (num<<1) + n
        if num%5 == 0:
            res.append(True)
        else:
            res.append(False)
    
    return res


assert prefixesDivBy52([0,1,1]) == [True,False,False]
assert prefixesDivBy52([1,1,1]) == [False,False,False]
