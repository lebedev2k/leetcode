from typing import List

def findWords(words: List[str]) -> List[str]:
    row1 =  set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")
    res = []
    for word in words:
        if row1.issuperset(word.lower()) or row2.issuperset(word.lower()) or row3.issuperset(word.lower()):
            res.append(word)
    return res
        
    
    

assert findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
assert findWords(["omk"]) == []
assert findWords(["adsdf","sfd"]) == ["adsdf","sfd"]