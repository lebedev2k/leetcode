from typing import List
from itertools import accumulate

def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    a = list(accumulate(arr, lambda a,b: a^b, initial=0))
    res = []
    for left, right in queries:
        res.append(a[right+1]^a[left])
    return res

