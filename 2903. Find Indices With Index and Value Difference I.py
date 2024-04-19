def findIndices(nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
    n = len(nums)
    for i in range(0, n-indexDifference): #0,1,2,3,4   2
        for j in range(i+indexDifference, n):
            if j-i>= indexDifference and abs(nums[j] - nums[i])>=valueDifference:
                return [i,j]
    return [-1, -1]

assert(findIndices([5,1,4,1], 2, 4) in ([0, 3], [3, 0]))
assert(findIndices([2,1], 0, 0) in ([0, 0], [0, 1], [1, 0], [1, 1]))
assert(findIndices([1,2,3], 2, 4) in ([-1, -1],))
