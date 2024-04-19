def sumBase(n: int, k: int) -> int:
    res = 0
    while n > 0:
        res += n % k
        n //= k 
    return res


assert sumBase(34,6) == 9
assert sumBase(10,10) == 1