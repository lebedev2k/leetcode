def minimumLength(s: str) -> int:
    l, r = 0, len(s)-1
    while l<r and s[l] == s[r]:
            c = s[l]
            while l<=r and s[l]==c:
                l += 1
            while l<=r and s[r]==c:
                r -= 1
    return r-l+1
 
def minimumLength2(s: str) -> int:
    l, r = 0, len(s)-1
    while l<r:
        if s[l] == s[r]:
            c = s[l]
            while l<=r and s[l]==c:
                l += 1
            while l<=r and s[r]==c:
                r -= 1
        else:
            return r-l+1
    return r-l+1           


assert minimumLength("bbbabbbccbcbcbccbbabbb") == 1
assert minimumLength("ca") == 2
assert minimumLength("cabaabac") == 0
assert minimumLength("aabccabba") == 3