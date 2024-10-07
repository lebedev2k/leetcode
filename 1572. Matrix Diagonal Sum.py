from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    summ, n = 0, len(mat)
    for i in range(n):
        summ += mat[i][i] + mat[i][n-1-i]
    if n%2 == 1: summ -= mat[n//2][n//2]        
            
    return summ

assert diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]) == 25

assert diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]) == 8

assert diagonalSum([[5]]) == 5