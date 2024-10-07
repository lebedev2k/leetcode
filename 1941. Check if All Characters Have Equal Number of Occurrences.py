from collections import Counter
def areOccurrencesEqual(s: str) -> bool:
    v = list(Counter(s).values())
    return  v.count(v[0]) == len(v)
    
    


assert areOccurrencesEqual("abacbc") == True
assert areOccurrencesEqual("aaabb") == False
    
    