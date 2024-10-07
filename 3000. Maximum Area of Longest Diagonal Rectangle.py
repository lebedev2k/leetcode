from typing import List

def areaOfMaxDiagonal(dimensions: List[List[int]]) -> int:
    longest_diag = 0
    max_square = 0
    for l,h in dimensions:
        d = l**2+h**2 
        if d > longest_diag:
            longest_diag = d
            max_square = l*h
        elif d == longest_diag and l*h > max_square:
            max_square = l*h
    return max_square 


assert areaOfMaxDiagonal([[9,3],[8,6]]) == 48
assert areaOfMaxDiagonal([[3,4],[4,3]]) == 12
