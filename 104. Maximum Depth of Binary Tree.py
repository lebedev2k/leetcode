class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    depth = 1
    q = [root]
    while q:
        newLevel = []
        for node in q:
            if node.left:
                newLevel.append(node.left)
            if node.right:
                newLevel.append(node.right)
        if newLevel:
            depth += 1
        q = newLevel
        
            
    return depth
        
    

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert maxDepth(root) == 3