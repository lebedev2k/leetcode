from typing import List
def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, k - 1
    a = min([nums[right+i]-nums[left+i] for i in range(len(nums)-k+1)])
    print(a)
    return a
    

minimumDifference([90], 1)
minimumDifference([9,4,1,7], 2)