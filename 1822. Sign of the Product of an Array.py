from typing import List

def arraySign(nums: List[int]) -> int:
    def signFunc(x):
        if x>0:
            return 1
        elif x<0:
            return -1
        return 0

    import operator
    from functools import reduce
    return signFunc(reduce(operator.mul, nums))


assert arraySign([-1,-2,-3,-4,3,2,1]) == 1
assert arraySign([1,5,0,2,-3]) == 0
assert arraySign([-1,1,-1,1,-1]) == -1