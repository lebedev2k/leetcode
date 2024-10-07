from typing import List

def minOperations(self, nums: List[int], k: int) -> int:
    pass


nums = [2,1,3,4]
k = 1
x = nums[0]
for i in range(1, len(nums)):
    x ^= nums[i]
    
    
print("{0:b}".format(x))         
print("{0:b}".format(x^k))         