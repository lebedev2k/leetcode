from typing import List

def findDuplicate(nums: List[int]) -> int:
    from collections import Counter
    counter = Counter(nums)
    return counter.most_common(1)[0][0]


def findDuplicate2(nums: List[int]) -> int:
    numstat = {}
    for n in nums:
        if n in numstat:
            return n
        numstat[n] = n
    return None
    


assert findDuplicate([1,3,4,2,2]) == 2
assert findDuplicate([3,1,3,4,2]) == 3
assert findDuplicate([3,3,3,3,3]) == 3
