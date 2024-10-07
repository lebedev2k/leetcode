def equalSubstring2(s: str, t: str, maxCost: int) -> int:
    ps = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
    left = 0
    n = len(s)
    while left < n and ps[left] > maxCost:
        left+=  1
    if left == n: return  0    
    maxLength  =  1  
    while left < len(s):
        right  = left+1
        summ = ps[left]
        while right < n and summ+ps[right] <= maxCost:
            summ += ps[right]
            right += 1
        maxLength = max(maxLength, right-left)
        left += 1
        
    return maxLength

from itertools import accumulate
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    
    ps = list(accumulate([abs(ord(s[i])-ord(t[i])) for i in range(len(s))]))
    print(ps)
    left = 0
    n = len(s)
    while left < n and ps[left] > maxCost:
        left+=  1
    if left == n: return  0    
    maxLength  =  1  
    while left < len(s):
        right  = left+1
        summ = ps[left]
        while right < n and summ+ps[right] <= maxCost:
            summ += ps[right]
            right += 1
        maxLength = max(maxLength, right-left)
        left += 1
        
    return maxLength        
        
        

assert equalSubstring("abcd", "bcdf", 3) == 3
assert equalSubstring("abcd",  "cdef",  1)  ==  0
assert equalSubstring("abcd",  "cdef",  3)  ==  1
assert equalSubstring("abcd",  "acde",  0)  ==  1
