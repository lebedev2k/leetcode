def isSubstringPresent(s: str) -> bool:
    reversed = s[::-1]
    h = set()
    for i in range(0, len(s)-1):
        h.add(reversed[i:i+2])
    for i in range(0, len(s)-1):
        s1 = s[i:i+2]
        if s1 in h:
            return True
    return False


assert isSubstringPresent("leetcode") == True
assert isSubstringPresent("abcba") == True
