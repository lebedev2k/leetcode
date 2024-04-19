from typing import List

def missingInteger(nums: List[int]) -> int:
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]+1:
            prefix_max_idx = i-1
            break
        prefix_sum += nums[i]

    nums_set = set(nums)    
    while True:
        if prefix_sum not in nums_set:
            return prefix_sum
        prefix_sum += 1  


assert missingInteger([46,8,2,4,1,4,10,2,4,10,2,5,7,3,1]) == 47
assert missingInteger([18,19,20,21,22,23,24,25,26,27,28,9]) == 253
assert missingInteger([29,30,31,32,33,34,35,36,37]) == 297
assert missingInteger([1,2,3,4,5]) == 15
assert missingInteger([1,2,3,2,5]) == 6
assert missingInteger([3,4,5,1,12,14,13]) == 15