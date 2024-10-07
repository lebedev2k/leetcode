from typing import List

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    for box in boxTypes:
        m = min(box[0], truckSize)
        total_units += m * box[1]
        truckSize -= m
        if truckSize == 0:
            break
    return total_units



assert maximumUnits([[1,3],[2,2],[3,1]], 4) == 8
assert maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10) == 91

