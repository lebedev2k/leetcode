from typing import List

def validMountainArray(arr: List[int]) -> bool:
    if len(arr) < 3: return False
    
    i = 1
    while i < len(arr) and arr[i] > arr[i-1]:
        i += 1
    if i == len(arr) or i == 1: return False
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1
    return i == len(arr)
    
        
        


assert validMountainArray([2, 1]) == False
assert validMountainArray([3, 5, 5]) == False
assert validMountainArray([0, 3, 2, 1]) == True
assert validMountainArray([0,1,2,3,4,5,6,7,8,9]) == False
assert validMountainArray([3, 2, 1, 0]) == False
assert validMountainArray([3, 2, 3, 4]) == False
