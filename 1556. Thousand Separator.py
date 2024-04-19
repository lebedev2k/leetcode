def thousandSeparator(n: int) -> str:
    s = str(n)
    n = len(s)
    res = ''
    while n-3>0:
        res = '.' + s[n-3:n] + res
        n -= 3
    return s[:n] + res
        

print(thousandSeparator(1234))
assert(thousandSeparator(987) == "987")
assert(thousandSeparator(1234) == "1.234")