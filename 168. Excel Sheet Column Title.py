def convertToTitle0(columnNumber: int) -> str:
    import string
    res = string.ascii_uppercase[columnNumber%26-1]
    r = 1
    k = 26
    while k<columnNumber:
        n = (columnNumber-26**r-1)%26
        res = string.ascii_uppercase[n] + res
        r += 1
        k += k*26
        
    return res


def convertToTitle(columnNumber: int) -> str:
    import string
    # res = string.ascii_uppercase[columnNumber%26-1]
    res = ''
    while columnNumber>0:
        columnNumber, n = divmod(columnNumber-1, 26)
        res = string.ascii_uppercase[n] + res
        
    return res


# assert convertToTitle(1) == "A"
# assert convertToTitle(28) == "AB"
# assert convertToTitle(701) == "ZY"
assert convertToTitle(2147483647) == "FXSHRXW"
