def isSumEqual2(firstWord: str, secondWord: str, targetWord: str) -> bool:
    k = ord('a')
    return int(''.join([str(ord(c)-k) for c in firstWord]))+int(''.join([str(ord(c)-k) for c in secondWord])) == int(''.join([str(ord(c)-k) for c in targetWord]))

def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    alphabet = 'abcdefghij'
    v = {c: str(ord(c)-ord('a')) for c in alphabet}
    return int(''.join([v[c] for c in firstWord]))+int(''.join([v[c] for c in secondWord])) == int(''.join([v[c] for c in targetWord]))



assert isSumEqual("acb", "cba", "cdb") == True
assert isSumEqual("aaa", "a", "aab") == False