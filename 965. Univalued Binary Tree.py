from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, unival):
            if not node: return True            
            if node.val != unival: return False
            
            b1 = dfs(node.left, unival)
            b2 = dfs(node.right, unival)
            return b1 and b2
            
        return dfs(root, root.val)
    
