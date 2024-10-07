import string
from collections import Counter

def sortString(s: str) -> str:
    res = ''
    c = Counter(s)
    chars = sorted(c.keys())
    hasChars = len(c)>0
    while hasChars:
        hasChars = False
        for i in range(len(chars)):
            if c.get(chars[i]):
                hasChars = True
                res += chars[i]
                c[chars[i]] = c[chars[i]]-1
        for i in range(len(chars)-1,-1,-1):
            if c.get(chars[i]):
                hasChars = True
                res += chars[i]
                c[chars[i]] = c[chars[i]]-1
    print(res)
    return res
                
    # n = len(s)
    # chars_forward = list(string.ascii_lowercase)
    # chars_backward = list(string.ascii_lowercase)[::-1]
    # while n:
    #     for ch in chars_forward:
    #         v = c.get(ch)
    #         if
        


assert sortString("aaaabbbbcccc") == "abccbaabccba"
assert sortString("rat") == "art"