from typing import List
from collections import Counter
def sortColors(nums: List[int]) -> None:
    c = Counter(nums)
    n0, n1, n2 = c.get(0) or 0, c.get(1) or 0, c.get(2) or 0   
    for i in range(n0):
        nums[i] = 0
    for i in range(n0, n0+n1):
        nums[i] = 1
    for i in range(n0+n1, n0+n1+n2):
        nums[i] = 2
    
a = [0,1,1,0]
sortColors(a)
print(a)

a = [2,0,2,1,1,0]
sortColors(a)
print(a)

a = [2,0,1]
sortColors(a)
print(a)