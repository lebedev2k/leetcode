def convertToTitle(columnNumber: int) -> str:
    import string
    l = list(string.ascii_uppercase)
    m = {i+1: l[i] for i in range(26)}
    
    

assert convertToTitle(1) == "A"
assert convertToTitle(28) == "AB"
assert convertToTitle(701) == "ZY"
