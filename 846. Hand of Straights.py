from typing import List
from collections import Counter

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize!= 0: return False
    # hand.sort()
    c = Counter(hand)
    nums = list(c.keys())
    nums.sort()
    i = 0
    while i< len(nums):
        if c.get(nums[i],  0)  ==  0: 
            i+=  1
            continue
        group = [nums[i]]
        c[nums[i]]  -=  1
        while len(group)< groupSize:
            v = c.get(group[-1]+1, 0)
            if not v: return False
            c[group[-1]+1]  -=  1
            group.append(group[-1]+1)
            
        # if c.get(nums[i],  0) == 0:
        #     i += 1
    return True
    
        

assert isNStraightHand([1,3,4,7,8,2,3,6,2], 3) == True
assert isNStraightHand([1,2,3,4,5],  4)  == False