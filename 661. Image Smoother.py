from typing import List

def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    from math import floor
    m = len(img)
    n = len(img[0])
    # if m==n and m==1:
    #     return img
    
    smoothedImg = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            s = 0
            columns = range(max(0, j-1), min(n, j+2))
            rows = range(max(0, i-1), min(m, i+2))
            for ii in rows:
                for jj in columns:
                   s += img[ii][jj]
             
            smoothedImg[i][j] = floor(s/(len(columns)*len(rows)))
    return smoothedImg    

assert imageSmoother([[1]]) == [[1]]
assert imageSmoother([[1,1,1],[1,0,1],[1,1,1]]) == [[0,0,0],[0,0,0],[0,0,0]]
assert imageSmoother([[100,200,100],[200,50,200],[100,200,100]]) == [[137,141,137],[141,138,141],[137,141,137]]