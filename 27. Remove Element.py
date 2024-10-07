from typing import List
def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = 101
        else:
            k += 1
    nums.sort()
    return k
            


assert removeElement([3,2,2,3], 3) == 2
assert removeElement([0,1,2,2,3,0,4,2],2) == 5
