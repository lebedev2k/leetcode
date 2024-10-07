from typing import List

def largestLocal2(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    res = [[0 for i in range(n-2)] for j in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            res[i][j] = max(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1],grid[i+2][j+2])
    return res

def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    res = []
    for i in range(n-2):
        row = []
        for j in range(n-2):
            row.append(max(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1],grid[i+2][j+2]))
        res.append(row)
            
    return res


assert largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) == [[9,9],[8,6]]
assert largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == [[2,2,2],[2,2,2],[2,2,2]]
