from typing import List

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    i = 0
    n = len(heights)
    while (bricks>0 or ladders>0) and i<n-1:
        if heights[i]<heights[i+1]:
            if heights[i+1]-heights[i]<=bricks:
                bricks -= heights[i+1]-heights[i]
            elif ladders>0:
                ladders -= 1
            else:
                break
        i += 1
    return i


assert furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4
assert furthestBuilding([14,3,19,3], 17, 0) == 3
assert furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7
