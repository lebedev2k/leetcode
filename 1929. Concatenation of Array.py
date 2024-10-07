from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums



print(getConcatenation([1,2,1]))