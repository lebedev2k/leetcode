def titleToNumber(columnTitle: str) -> int:
    n = len(columnTitle)
    offset = ord('A') - 1
    num = 0
    for i in range(n):
        num += (ord(columnTitle[n-i-1]) - offset) * 26**i
    return num

assert titleToNumber("ZY") == 701
assert titleToNumber("A") == 1  
assert titleToNumber("AB") == 28
