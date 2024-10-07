
def reformat(s: str) -> str:
    letters = []
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)
        else:
            letters.append(c)
    if len(letters)-len(digits) not in [-1,0,1]:
        return ""
    
    res = ""
    if len(letters)>len(digits):
        res += letters.pop(0)
        for i in range(len(letters)):
            res += digits[i]
            res += letters[i]
    elif len(letters)<len(digits):
        res += letters.pop(0)
        for i in range(len(letters)):
            res += letters[i]
            res += digits[i]
    else:
        for i in range(len(letters)):
            res += letters[i]
            res += digits[i]
        
    return res



assert reformat("a0b1c2") in ("0a1b2c","0a1b2c","a0b1c2","0a1b2c","0c2a1b")