#https://leetcode.com/problems/pascals-triangle/

#https://leetcode.com/problems/pascals-triangle/submissions/1084500939/


def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    for i in range(1, numRows-1):
        new_row = [1]
        middle = [res[i][j]+res[i][j+1] for j in range(len(res[i])-1)]
        new_row.extend(middle)
        new_row.append(1)
        res.append(new_row)
    return res


print(generate(5))
