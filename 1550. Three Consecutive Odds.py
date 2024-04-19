from typing import List

def threeConsecutiveOdds(arr: List[int]) -> bool:
    counter = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return True
    return False               


assert threeConsecutiveOdds([2,6,4,1]) == False
assert threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]) == True