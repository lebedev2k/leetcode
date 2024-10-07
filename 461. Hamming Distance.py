def hammingDistance(x: int, y: int) -> int:
    return sum(map(int, format(x ^ y,'b')))


assert hammingDistance(1, 4) == 2
assert hammingDistance(3, 1) == 1