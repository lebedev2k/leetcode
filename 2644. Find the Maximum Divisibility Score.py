from typing import List

def maxDivScore(nums: List[int], divisors: List[int]) -> int:
    scores = [0] * len(divisors)
    for i, divisor in enumerate(divisors):
        for num in nums:
            if num % divisor == 0:
                scores[i] += 1
    m = max(scores)
    return min([divisors[i] for i in range(len(scores)) if scores[i] == m])



assert maxDivScore([2,9,15,50], [5,3,7,2]) == 2
assert maxDivScore([4,7,9,3,9], [5,2,3]) == 3
assert maxDivScore([20,14,21,10], [10,16,20]) == 10