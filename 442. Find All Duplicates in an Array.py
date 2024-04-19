from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    stat = [0]*(len(nums)+1)
    res = []
    for n in nums:
        stat[n] += 1
        if stat[n] == 2:
            res.append(n)
    return res
    


assert findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
assert findDuplicates([1,1,2]) == [1]
assert findDuplicates([1]) == []