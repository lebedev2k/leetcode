def scoreOfString(s: str) -> int:
    return sum([abs(ord(s[i])-ord(s[i+1])) for i in range(0,len(s)-1)])


assert scoreOfString("hello") == 13
assert scoreOfString("zaz") == 50
 