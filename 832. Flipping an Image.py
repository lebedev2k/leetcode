from typing import List

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for i, row in enumerate(image):
        image[i] = list(map(lambda x: not x, row[::-1]))
    return image

map(lambda x: not x, [1,0,1])
assert flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
assert flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]