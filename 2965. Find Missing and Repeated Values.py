from typing import List

def findMissingAndRepeatedValues2(grid: List[List[int]]) -> List[int]:
    from collections import defaultdict
    d = defaultdict(int)
    for i in grid:
        for j in i:
            d[j] += 1
    dbl = [k for k,v in d.items() if v>1]
    absent = set([i for i in range(1,len(grid)**2+1)]) - set(d.keys())  
    return [dbl[0], absent.pop()]            
    
def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    g = [j for i in grid for j in i]
    ans = []

    ans.append(sum(g) - sum(set(g)))
    ans.append(sum(range(1, len(g)+1)) - sum(set(g)))
    # if ans[1] == 0:
    #     ans[1] = max(g)+1

    return ans
        
assert findMissingAndRepeatedValues([[1,3],[2,2]]) == [2,4]
assert findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]) == [9,5]

