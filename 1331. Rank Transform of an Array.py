from typing import List
def arrayRankTransform(arr: List[int]) -> List[int]:
    a = sorted(zip(arr, range(len(arr))))
    res = [0] * len(arr)
    rank = 1
    for i in range(1, len(a)):
        res[a[i-1][1]] = rank
        if a[i][0] != a[i-1][0]:
            rank += 1       
    res[a[-1][1]] = rank
    return res


print(arrayRankTransform([40,10,20,30]))
print(arrayRankTransform([100,100,100,100]))