from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    new_matrix = [[] for i in range(len(matrix[0]))]  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j].append(matrix[i][j])
                
    return new_matrix


assert transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]