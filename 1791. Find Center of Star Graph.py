from typing import List
from collections import defaultdict
def findCenter(edges: List[List[int]]) -> int:
    graph = defaultdict(int)
    for edge in edges:
        graph[edge[0]] += 1
        graph[edge[1]] += 1
    for key, value in graph.items():
        if value == len(edges):
            return key



assert findCenter([[1,2],[2,3],[4,2]]) == 2
assert findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1
