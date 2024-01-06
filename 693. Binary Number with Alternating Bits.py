def hasAlternatingBits(n: int) -> bool:
    num = n & 1
    while n:
        n >>= 1
        nextnum = n & 1
        if n and nextnum == num:
            return False
        num = nextnum
    return True

assert(hasAlternatingBits(5) == True)
assert(hasAlternatingBits(7) == False)
assert(hasAlternatingBits(11) == False)