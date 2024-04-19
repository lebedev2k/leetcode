def thirdMax(nums: list[int]) -> int:
    s = set(nums)
    if len(s)<3:
        return max(nums)
    a = sorted(list(s))
    return a[-3]
    


assert thirdMax([3,2,1]) == 1
assert thirdMax([1,2]) == 2
assert thirdMax([2,2,3,1]) == 1
