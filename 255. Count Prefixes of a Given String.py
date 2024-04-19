from typing import List
def countPrefixes(words: List[str], s: str) -> int:
    return sum(1 for x in words if s.startswith(x))

def countPrefixes2(words: List[str], s: str) -> int:
    res = 0
    for x in words:
        if s.startswith(x):
            res += 1
    return res

assert countPrefixes(["a","b","c","ab","bc","abc"], "abc") == 3
assert countPrefixes(["a","a"], "aa") == 2