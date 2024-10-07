
def minimumPushes(word: str) -> int:
    if len(word) <= 8:
        return len(word)
    k,v = divmod(len(word), 8)
    return 8*sum(i for i in range(k+1)) + (k+1)*v
#8*1+8*2+8*3    

assert minimumPushes("abhrlngxyjkezwcm") == 24
assert minimumPushes("abcde") == 5
assert minimumPushes("xycdefghij") == 12