from typing import List
from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    result = []
    for k1, v1 in c1.items():
        if k1 in c2:
            result.extend([k1] * min(v1, c2[k1]))
    return result


print(intersect([1,2,2,1], [2,2]))
print(intersect([4,9,5], [9,4,9,8,4]))