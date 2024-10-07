from typing import List
def numberOfAlternatingGroups(colors: List[int]) -> int:
    
    res = int((colors[-1]==1 and colors[0]==0 and colors[1]==1) or (colors[-1]==0 and colors[0]==1 and colors[1]==0))
    res += int((colors[-2]==1 and colors[-1]==0 and colors[0]==1) or (colors[-2]==0 and colors[-1]==1 and colors[0]==0))
    for i in range(1,len(colors)-1):
        res += int((colors[i-1]==1 and colors[i]==0 and colors[i+1]==1) or (colors[i-1]==0 and colors[i]==1 and colors[i+1]==0))
    return res
        

assert numberOfAlternatingGroups([0,1,0,0,1]) == 3
assert numberOfAlternatingGroups([1,1,1]) == 0

