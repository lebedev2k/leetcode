from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    search = True
    for interval in intervals:
        if search:
            if interval[0]<=newInterval[1] and interval[1]>=newInterval[0]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            elif newInterval[0]<interval[0]:
                res.append(newInterval)
                res.append(interval)
                search = False
            else:
                res.append(interval)
        else:
            res.append(interval)
    if search:
        res.append(newInterval)
    print(res)
    return res


# insert([[1,3],[6,9]], [2,5])
insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])