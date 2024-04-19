from typing import List
def findJudge(n: int, trust: List[List[int]]) -> int:
    a = list(set([i for i in range(1, n+1)]) - set([t[0] for t in trust]))
    if len(a) == 1 and [t[1] for t in trust].count(a[0]) == n-1:
        return a[0]
    return -1    


assert findJudge(2, [[1,2]]) == 2
assert findJudge(3, [[1,3],[2,3]]) == 3
assert findJudge(3, [[1,3],[2,3],[3,1]]) == -1
assert findJudge(3, [[1,2],[2,3]]) == -1
