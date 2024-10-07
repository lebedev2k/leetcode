class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import defaultdict


def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes_tbl = defaultdict(list)
    node_values = set()
    
    for desc in descriptions:
        if desc[0] not in nodes_tbl:
            nodes_tbl[desc[0]] = TreeNode(desc[0])
            node_values.add(desc[0])
        if desc[1] not in nodes_tbl:
            nodes_tbl[desc[1]] = TreeNode(desc[1])
            node_values.add(desc[0])
    
    for desc in descriptions:
        parent = nodes_tbl[desc[0]]
        child = nodes_tbl[desc[1]]
        if desc[2] == 1:
            parent.left = child
        else:
            parent.right = child
        node_values.discard(desc[1])
    return nodes_tbl[node_values.pop()]
                



    return (parents & childs).pop()

createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])