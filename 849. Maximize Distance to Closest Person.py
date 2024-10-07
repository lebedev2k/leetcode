#FAIL ON TEST 61
# 0 1 0 0 0 0 0 0 1 1 0 1 1
# expected: 3
# output: 5

from typing import List
def maxDistToClosest(seats: List[int]) -> int:
    empty_seats = []
    a = [i for i, v in enumerate(seats) if v==1]
    if a[0]>0: 
        empty_seats.append(a[0])
    for i in range(1,len(a)):
        v = a[i]-a[i-1]-1
        if v>1: 
            empty_seats.append(v-1)
        else:
            empty_seats.append(v)
    if seats[-1] == 0: 
        empty_seats.append(len(seats) - a[-1] - 1)
    # print(empty_seats)
    return max(empty_seats)


assert maxDistToClosest([1,0,1]) == 1
assert maxDistToClosest([1,0,0,0,1,0,1]) == 2
assert maxDistToClosest([1,0,0,0]) == 3
assert maxDistToClosest([0,1]) == 1

