def minStartValue(nums: list[int]) -> int:
    from itertools import accumulate
    i = 1
    while True:
        if min(accumulate(nums, initial = i))>0:
            return i
        i += 1

def minStartValue2(nums: list[int]) -> int:
    from itertools import accumulate
    i = 1
    while True:
        f = True
        s = i
        for num in nums:
            s += num
            if s<=0:
                f = False 
                break       
        if f:
            return i
        i += 1

assert(minStartValue2([-3,2,-3,4,2]) == 5)
assert(minStartValue2([1,2]) == 1)
assert(minStartValue2([1,-2,-3]) == 5)
