from typing import List
from collections import defaultdict

def getMaximumGold(grid: List[List[int]]) -> int:
    def find_paths(grid: list, u: tuple, visited: dict, gold_mined: int):
        nonlocal maxgold, visited_all
        visited[u] = 1
        visited_all[u] = 1
        gold_mined += grid[u[0]][u[1]]
        
        for v in [(0,1), (1,0), (0,-1), (-1,0)]:
            if 0 <= u[0]+v[0] < len(grid) and 0 <= u[1]+v[1] < len(grid[0]) and grid[u[0]+v[0]][u[1]+v[1]] != 0 and (u[0]+v[0], u[1]+v[1]) not in visited:
                find_paths(grid, (u[0]+v[0], u[1]+v[1]), visited, gold_mined)
                
        maxgold = max(maxgold, gold_mined)
        gold_mined -= grid[u[0]][u[1]]
        visited.pop(u)

        


    visited = defaultdict(int)
    visited_all = defaultdict(int)
    maxgold = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0: # and (i,j) not in visited_all
                find_paths(grid, (i,j), visited, 0)
            # find_paths(grid, (2,1), visited, 0)
    return maxgold




print(getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
assert(getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]) == 24)

print(getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
assert(getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]) == 28)