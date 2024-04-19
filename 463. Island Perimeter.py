from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    island_points = [(i,j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1]
    edges = 0
    for i,j in island_points:
        if i == 0 or grid[i-1][j] == 0:
            edges += 1
        if i == len(grid)-1 or grid[i+1][j] == 0:
            edges += 1
        if j == 0 or grid[i][j-1] == 0:
            edges += 1
        if j == len(grid[i])-1 or grid[i][j+1] == 0:
            edges += 1
    return edges
                                
                                
        


assert islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
assert islandPerimeter([[1]]) == 4
assert islandPerimeter([[1,0]]) == 4