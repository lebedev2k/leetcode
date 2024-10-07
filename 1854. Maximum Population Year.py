from typing import List
from collections import defaultdict, Counter
def maximumPopulation(logs: List[List[int]]) -> int:
    cnt = defaultdict(int)
    for log in logs:
        for year in range(log[0], log[1]):
            cnt[year] += 1
    max_population = max(cnt.values())
    return min(year for year, population in cnt.items() if population == max_population)



assert maximumPopulation([[1993,1999],[2000,2010]]) == 1993
assert maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]) == 1960
