from typing import List

def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
    all_path = sum(distance)
    if start<=destination:
        d1 = sum(distance[start:destination])        
    else:
        d1 = sum(distance[start:])+sum(distance[:destination])
    return min (all_path-d1,d1)


assert distanceBetweenBusStops([1,2,3,4], 0, 1) == 1
assert distanceBetweenBusStops([1,2,3,4], 0, 2) == 3
assert distanceBetweenBusStops([1,2,3,4], 0, 3) == 4
