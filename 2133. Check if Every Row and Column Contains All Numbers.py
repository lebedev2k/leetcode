from typing import List

def checkValid(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    for i in range(n):
        if len(set(matrix[i])) != n:
            return False
    
    for j in range(n):
        col = set()
        for i in range(n):
           col.add(matrix[i][j]) 
        if len(col) != n:
            return False
    
    return True
        

def checkValid2(matrix: List[List[int]]) -> bool:
    for j in range(len(matrix)):
        col = set()
        for i in range(len(matrix)):
            if len(set(matrix[i])) != len(matrix[i]):
                return False
            col.add(matrix[i][j]) 
        if len(col) != len(matrix[j]):
            return False

    return True

assert checkValid([[1,2,3],[3,1,2],[2,3,1]]) == True
assert checkValid([[1,1,1],[1,2,3],[1,2,3]]) == False