from typing import List
def minCostClimbingStairs(cost: List[int]) -> int:
    i = 0
    total_cost = 0
    while i>=len(cost):
        if cost[i]<cost[i+1]:
            total_cost += cost[i]
            i += 1
        else:
            total_cost += cost[i+1]
            i += 2
    return total_cost
    


assert minCostClimbingStairs([10,15,20]) == 15
assert minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6