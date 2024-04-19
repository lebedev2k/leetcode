from typing import List

def getCommon(nums1: List[int], nums2: List[int]) -> int:
    i = j = 0
    while i<len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]
        if nums1[i]<nums2[j]:
            i+=1
        else:
            j+=1
    return -1


assert getCommon([1,2,3], [2,4]) == 2
assert getCommon([1,2,3,6], [2,3,4,5]) == 2
