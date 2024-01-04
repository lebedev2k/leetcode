#https://leetcode.com/problems/assign-cookies/


def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    n = j = i = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            n += 1
            i += 1
        j += 1
    return n


assert(findContentChildren([1,2,3], [1,1]) == 1)
assert(findContentChildren([1,2], [1,2,3]) == 2)
assert(findContentChildren([1,2,3], [3]) == 1)