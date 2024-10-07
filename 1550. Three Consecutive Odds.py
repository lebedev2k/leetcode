from typing import List
def threeConsecutiveOdds(arr: List[int]) -> bool:
    if len(arr) < 3: return False
    for i in range(len(arr)-2):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i] % 2 == 1:
            return True
    return False               


def threeConsecutiveOdds2(arr: List[int]) -> bool:
    counter = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
    return False               


assert threeConsecutiveOdds([2,6]) == False
assert threeConsecutiveOdds([1,3,5]) == True
assert threeConsecutiveOdds([2,6,4,1]) == False
assert threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]) == True