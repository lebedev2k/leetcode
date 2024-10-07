from collections import defaultdict
def countPoints(rings: str) -> int:
    rods = defaultdict(set)
    for i in range(0,len(rings),2):
        rods[rings[i+1]].add(rings[i])
    return sum([1 for v in rods.values() if len(v) == 3])