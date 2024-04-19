def firstUniqChar(s: str) -> int:
    from collections import defaultdict
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    a = [x[0] for x in list(filter(lambda x: len(x)==1, d.values()))]
    
    return min(a, default=-1)
    # return max(-1, min(a, default=-1))

assert firstUniqChar("leetcode") == 0
assert firstUniqChar("loveleetcode") == 2
assert firstUniqChar("aabb") == -1