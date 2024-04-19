from typing import List

#optimal (not me)
def findMinArrowShots2(points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                end = point[1]
                arrow += 1
        return arrow


def findMinArrowShots(points: List[List[int]]) -> int:
    cnt = 1
    points.sort()
    cur_range = points[0]
    for i in range(1,len(points)):
        if points[i][0]<=cur_range[1] and points[i][1]>=cur_range[0]:
                cur_range[0] = max(points[i][0], cur_range[0])
                cur_range[1] = min(points[i][1], cur_range[1])
        else:
            cnt += 1
            cur_range = points[i]
    return cnt    

assert findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
assert findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
assert findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2