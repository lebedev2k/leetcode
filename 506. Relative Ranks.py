from typing import List

def findRelativeRanks( score: List[int]) -> List[str]:
    a = []
    for i, value in enumerate(score):
        a.append((value, i))
    a.sort(reverse=True)
    for i in range(len(a)):
        if i == 0:
            score[a[i][1]] = "Gold Medal"
        elif i == 1:
            score[a[i][1]] = "Silver Medal"
        elif i == 2:
            score[a[i][1]] = "Bronze Medal"
        else:
            score[a[i][1]] = str(i+1)
    return score
        


assert findRelativeRanks([5,4,3,2,1]) == ["Gold Medal","Silver Medal","Bronze Medal","4","5"]