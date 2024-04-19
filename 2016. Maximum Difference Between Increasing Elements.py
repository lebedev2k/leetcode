def maximumDifference(nums: list[int]) -> int:
    max_diff = 0
    for i in range(len(nums)-1):
        m = max(nums[i+1:])
        max_diff = max(max_diff, m - nums[i])
        # if m - nums[i] > max_diff:
        #     max_diff = m - nums[i]
    
    return max_diff if max_diff>0 else -1
        
assert(maximumDifference([7,1,5,4]) == 4)
assert(maximumDifference([9,4,3,2]) == -1)
assert(maximumDifference([1,5,2,10]) == 9)