from typing import List

def arithmeticTriplets(nums: List[int], diff: int) -> int:
    n = len(nums)
    counter = 0
    for i in range(len(nums)-2):
        triplet = set([nums[i]])
        for j in range(i+1, n):
            if nums[j]-nums[i] == diff:
                triplet.add(nums[j])
                for k in range(j+1, n):
                    if nums[k]-nums[j] == diff:
                        counter += 1
                triplet.remove(nums[j])

    return counter

assert arithmeticTriplets([0,1,4,6,7,10], 3) == 2
assert arithmeticTriplets([4,5,6,7,8,9], 2) == 2
