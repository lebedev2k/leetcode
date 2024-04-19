from typing import List

def shortestToChar(s: str, c: str) -> List[int]:
    res = [0] * len(s)
    idx = [i for i in range(len(s)) if c==s[i]]
    left, right = -1, 0
    for i in range(len(s)):
        pass

assert shortestToChar("loveleetcode", "e") == [3,2,1,0,1,0,0,1,2,2,1,0]