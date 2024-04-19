from typing import List

def maximumNumberOfStringPairs(words: List[str]) -> int:
    v = {}
    for word in words:
        reverse_word = word[::-1]
        if reverse_word in v:
            v[reverse_word] += 1
        else:
            v[word] = 0
    return sum(v.values())


assert maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]) == 2
assert maximumNumberOfStringPairs(["ab","ba","cc"]) == 1
assert maximumNumberOfStringPairs(["aa","ab"]) == 0