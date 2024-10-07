from typing import List

def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    i, j = 0, 0
    max_profit = 0
    res = 0
    while i < len(worker) and j < len(jobs):
        if worker[i] >= jobs[j][0]:
            max_profit = max(max_profit, jobs[j][1])
            j += 1
        else:
            res += max_profit
            i += 1
    if j == len(jobs):res  += max_profit*(len(worker)-i)

    return res
            


assert maxProfitAssignment([7,20,68], [26,28,57], [71,20,71]) == 142
assert maxProfitAssignment([13,37,58], [4,90,96], [34,73,45]) == 190
assert maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]) == 100
assert maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]) == 0