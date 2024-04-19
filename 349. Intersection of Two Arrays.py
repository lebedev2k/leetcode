from typing import List 

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
   
    if len(nums1)<len(nums2):
        return list({n: n for n in nums1 if n in nums2}.keys())
    else:
        return list({n: n for n in nums2 if n in nums1}.keys())

def intersection2(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
    

assert intersection2([1,2,2,1], [2,2]) == [2]
assert intersection2([4,9,5], [9,4,9,8,4]) == [9,4] # [4,9]