from typing import List

def captureForts(forts: List[int]) -> int:
    i = j = 0
    n = len(forts)
    maxForts = 0
    while j<n:
        while i<n and forts[i] not in (-1,1):
            i += 1
        j = i+1
        while j<n and forts[j] not in (-1,1):
            j += 1
        if j<n:
            if forts[i]+forts[j] == 0 and j>i+1:
                maxForts = max(maxForts, j-i-1)     
            i = j
            j = i+1
        else:
            break
    return maxForts
        
        


assert captureForts([1,0,0,-1,0,0,0,0,1]) == 4
assert captureForts([0,0,1,-1]) == 0