from typing import List
import queue

def timeRequiredToBuy2(tickets: List[int], k: int) -> int:
    time = 0
    for _ in range(tickets[k]):
        for i in range(len(tickets)):
            if tickets[i]>0:
                time += 1
                tickets[i] -= 1
    return time
        

def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = k+1
    tickets[k] -= 1
        
    for i in range(len(tickets)):
        if i<k:
            tickets[i] -= 1
        time += min(tickets[i], tickets[k])            
    return time


assert timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3) == 154
assert timeRequiredToBuy([2, 3, 2], 2) == 6
assert timeRequiredToBuy([5, 1, 1, 1], 0) == 8

