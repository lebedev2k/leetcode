from typing import List
def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    for x in range(left, right+1):
        b = False
        for start, end in ranges:
            if x>=start and x<=end:
                b = True
                break
        if not b:
            return False
    return True


assert isCovered([[1,2],[3,4],[5,6]], 2, 5) == True
assert isCovered([[1,10],[10,20]], 21, 21) == False
