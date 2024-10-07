from typing import List
def countCompleteDayPairs(hours: List[int]) -> int:
    cnt = 0
    for i in range(len(hours)-1):
        for j in range(i+1, len(hours)):
            if (hours[i]+hours[j]) % 24 == 0:
                cnt += 1
    return cnt


assert countCompleteDayPairs([12,12,30,24,24]) == 2
assert countCompleteDayPairs([72,48,24,3]) == 3