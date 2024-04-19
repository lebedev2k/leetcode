def isPowerOfTwo(n: int) -> bool:
    return bin(n).count('1')==1


assert isPowerOfTwo(1) == True
assert isPowerOfTwo(16) == True
assert isPowerOfTwo(3) == False
    