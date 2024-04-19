def findPeaks(mountain: list[int]) -> list[int]:
    n = len(mountain)
    i = 1
    res = []
    while i < n-1:
        if mountain[i] > mountain[i+1]:
            if mountain[i-1] < mountain[i]:
                res.append(i)
            i += 2
        else:
            i += 1
    return res
    #интересное решение
    #  return [idx +1 for idx, (a,b,c) in enumerate(zip(mountain, mountain[1:], mountain[2:])) if a<b>c] 
            

assert(findPeaks([2,4,4]) == [])
assert(findPeaks([1,4,3,8,5]) == [1, 3])
