from typing import List
def deleteGreatestValue(grid: List[List[int]]) -> int:
    for row in grid:row.sort()
    res = 0
    for i in range(len(grid[0])):
        m = grid[0][-1]
        for row in grid:
            if row[-1]>m:
                m = row[-1]
            del row[-1]
        res += m
    return res


assert deleteGreatestValue([[1,2,4],[3,3,1]]) == 8