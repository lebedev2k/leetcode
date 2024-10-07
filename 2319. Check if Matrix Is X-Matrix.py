from typing import List

def checkXMatrix(grid: List[List[int]]) -> bool:
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if (i == j or i+j+1 == n):
                if grid[i][j] == 0:
                    return False
            elif grid[i][j] != 0:
                return False
    return True


assert checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]) == True
assert checkXMatrix([[5,7,0],[0,3,1],[0,5,0]]) == False

    