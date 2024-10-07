from typing import List

def duplicateZeros(arr: List[int]) -> None:
    i, n = 0, len(arr)
    while i<n:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1
            
arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)  

arr = [1,2,3]
duplicateZeros(arr)
print(arr)  