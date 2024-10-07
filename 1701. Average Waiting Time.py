from typing import List
def averageWaitingTime(customers: List[List[int]]) -> float:
    waiting_times = 0
    last_time = customers[0][0]
    for arrive_time, wait_time in customers:
        last_time = max(arrive_time, last_time) + wait_time
        waiting_times += last_time-arrive_time
    return waiting_times/len(customers)
        


assert averageWaitingTime([[1,2],[2,5],[4,3]]) == 5.0
assert averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]) == 3.25