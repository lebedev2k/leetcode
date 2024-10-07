from typing import List
def reverseString(s: List[str]) -> None:
    for i in range(len(s)//2):
        s[i], s[-i-1] = s[-i-1], s[i]
        

s = ["h","e","l","l","o"]
reverseString(s)
print(s)
s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)
                
        
