from typing import List
def findMinDifference(timePoints: List[str]) -> int:
    times = []
    for time in timePoints:
        h, m = map(int, time.split(':'))
        times.append(60*h+m)
    times.sort()
    min_diff = times[0] + (24*60-times[-1])
    for i in range(len(times)-1):
        min_diff = min(min_diff, times[i+1]-times[i])
    return min_diff


assert findMinDifference(["23:59","00:00"]) == 1
assert findMinDifference(["00:00","23:59","00:00"]) == 0