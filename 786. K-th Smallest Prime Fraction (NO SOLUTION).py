from typing import List

#проходит не все тесты
def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    res = [(arr[0], arr[-1])]
    i, j = 0, len(arr) - 1
    while len(res) < k and i < j:
        if arr[i]/arr[j-1]< arr[i+1]/arr[j]:
            res.append((arr[i], arr[j-1]))
            res.append((arr[i+1], arr[j]))
        else:
            res.append((arr[i+1], arr[j]))
            res.append((arr[i], arr[j-1]))
        j -= 1
        i += 1
    
    return res[k - 1]


assert kthSmallestPrimeFraction([1,13,17,59], 6) == (13,17)
assert kthSmallestPrimeFraction([1,2,3,5], 3) == (2,5)
assert kthSmallestPrimeFraction([1,7], 1) == (1,7) 