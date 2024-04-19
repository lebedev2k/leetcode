def finalString(s: str) -> str:
    from collections import deque
    res = deque()
    i = 0
    for c in s:
        if c != 'i':
            if i%2 == 0:
                res.append(c)
            else:
                res.appendleft(c)
        else:
            i += 1
    if i%2 == 0:
        return ''.join(res)
    res.reverse()
    return ''.join(res)
    


assert finalString("string") == "rtsng"
assert finalString("poiinter") == "ponter"
