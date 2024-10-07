from typing import List

def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    prefixes = {}
    longest_prefix_len1 = 0
    for n in arr1:
        prefix = ''
        for c in str(n):
            prefix += c
            if prefix not in prefixes:
                prefixes[prefix] = 1
                longest_prefix_len1 = max(longest_prefix_len1, len(prefix))
    longest_prefix_len = 0
    for n in arr2:
        prefix = ''
        n = str(n)
        for i in range(min(len(n), longest_prefix_len1)):
            prefix += n[i]
            if prefix in prefixes:
                longest_prefix_len = max(longest_prefix_len, len(prefix))
    return longest_prefix_len


assert longestCommonPrefix([1,10,100], [1000]) == 3
assert longestCommonPrefix([1,2,3], [4,4,4]) == 0