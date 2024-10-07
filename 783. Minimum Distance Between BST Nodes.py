class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

def minDiffInBST(root: Optional[TreeNode]) -> int:
    def dfs(node,values):
        if not node: return
        values.append(node.val)
        dfs(node.left, values)
        dfs(node.right, values)
    
    values = []
    dfs(root, values)
    values.sort()
    mindiff = values[1]-values[0]
    for i in range(1, len(values)-1):
        mindiff = min(mindiff, values[i+1]-values[i])
    return mindiff
