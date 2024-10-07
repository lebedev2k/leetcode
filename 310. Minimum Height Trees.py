from typing import List

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    from collections import defaultdict
    
    if not edges:
        return 0
    
    def bfs(node, heights: List, done: set):       
        child_nodes = []
        for n in tree[node]:
            if n not in done:
                child_nodes.append(n)
                done.add(n)
        
        if not child_nodes:
            return 0
        
        for n in child_nodes:
                h = bfs(n, heights, done)
                heights.append(h)
        
        return max(heights) + 1
                                
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    heights = defaultdict(list)
    
    for node in tree.keys():
        heights[bfs(node, [],set([node]))].append(node)
        
    return heights[min(heights.keys())]
    


print(findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])) #[3]
print(findMinHeightTrees(1, [])) #[0]
print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
