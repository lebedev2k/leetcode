from typing import List

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    
    visited = [False] * n
    q = deque()
    q.append(source)
    while q:
        node = q.popleft()
        if node == destination:
            return True
        visited[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                q.append(neighbour)
    return False


