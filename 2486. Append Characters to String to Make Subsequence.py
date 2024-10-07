def appendCharacters(s: str, t: str) -> int:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i  +=  1
            j  +=  1
        else:
            i  +=  1
    return len(t) - j



assert appendCharacters("coaching", "coding") == 4
assert appendCharacters("abcde", "a") == 0
assert appendCharacters("z", "abcde") == 5