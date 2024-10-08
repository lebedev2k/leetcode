from typing import List
def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    from collections import Counter
    c = Counter(arr1)
    res = []
    res2 = []
    for n in arr2:
        if n in c:
            res.extend([n for _ in range(c.pop(n))])
    for n in c:
        res2.extend([n for _ in range(c[n])])

    res2.sort()
    res.extend(res2)
    
    return res
    


assert relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
assert relativeSortArray([28,6,22,8,44,17], [22,28,8,6]) == [22,28,8,6,17,44]