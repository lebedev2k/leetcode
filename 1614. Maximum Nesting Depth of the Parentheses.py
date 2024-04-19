def maxDepth(s: str) -> int:
    maxx = 0
    cnt = 0
    for c in s:
        if c=='(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        maxx = max(maxx, cnt)
    return maxx


# def maxDepth(s: str) -> int:
#     from itertools import accumulate
#     accumulate([])


assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert maxDepth("(1)+((2))+(((3)))") == 3
assert maxDepth("") == 0