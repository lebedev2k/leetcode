from collections import Counter
from itertools import accumulate

def equalFrequency(word: str) -> bool:
    c = Counter(word)
    s = set(c.values())
    if len(s)==1 and len(c)>1:
        return False
    elif len(s)==1 and len(c)==1:
        return True
    
    d = list(c.values())
    d.sort()
    if d[0]
    


assert equalFrequency("abcc") == True
assert equalFrequency("aazz") == False