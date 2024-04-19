def rowAndMaximumOnes(mat: list[list[int]]) -> list[int]:
    res = []
    m, n = 0, 0
    for i, row in enumerate(mat):
        rowsum = sum(row)
        if rowsum>m:
            m = rowsum
            n = i
        res.append(rowsum)
    return [n, res[n]]

assert rowAndMaximumOnes([[0,1],[1,0]]) == [0,1]
assert rowAndMaximumOnes([[0,0,0],[0,1,1]]) == [1,2]    
assert rowAndMaximumOnes([[0,0],[1,1],[0,0]]) == [1,2]    