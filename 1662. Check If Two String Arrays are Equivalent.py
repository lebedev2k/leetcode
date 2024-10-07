from typing import List
def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)


assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) == True
assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) == False
assert arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True