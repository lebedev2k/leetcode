from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([n**2 for n in nums])


assert sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]