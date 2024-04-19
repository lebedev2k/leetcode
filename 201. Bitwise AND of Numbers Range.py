def rangeBitwiseAnd(left: int, right: int) -> int:
    res = ''
    r = right
    n = 0
    while r>=left and r > 0:
        if r & 1 == 0:
            res = '0' + res
            r = right
            n += 1
            r >>= n
            left >>= 1
        elif r == left:
            res = '1' + res
            r = right
            n += 1
            r >>= n
            left >>= 1
        else:       
            r -= 1
    
    return int(res,2) if  res else 0


assert rangeBitwiseAnd(5,7) == 4
assert rangeBitwiseAnd(0,0) == 0
assert rangeBitwiseAnd(1,2147483647) == 0