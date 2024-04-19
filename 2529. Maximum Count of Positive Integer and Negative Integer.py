def maximumCount(nums: list[int]) -> int:
    zero, neg = 0, 0
    for i in range(len(nums)):
        if nums[i]<0:
            neg += 1
        elif nums[i]>0:
            return max(neg, len(nums)-i) #нет необходимости считать положительные числа
        else:
            zero += 1
    return len(nums)-zero #сюда придем, если в последовательности нет положит.чисел
            
def maximumCount2(nums: list[int]) -> int:
    nums = []

def maximumCount3(nums: list[int]) -> int:
    return max(
            len([x for x in nums if x < 0]),
            len([x for x in nums if x > 0])
        )
            

assert(maximumCount([-2,-1,-1,1,2,3])==3)
assert(maximumCount([-3,-2,-1,0,0,1,2])==3)
assert(maximumCount([5,20,66,1314])==4)