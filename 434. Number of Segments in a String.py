import typing

def countSegments(s: str) -> int:
    return len(s.split()) if len(s) else 0

def countSegments2(s: str) -> int:
    n = len(s)
    i = 0
    words = 0 
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        if i < n:
            words += 1
        while i < n and s[i] != ' ':
            i += 1

    return words


assert countSegments2("Hello, my name is John") == 5
assert countSegments2("Hello") == 1