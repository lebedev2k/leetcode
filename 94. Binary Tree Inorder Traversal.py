class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def dfs(root: Optional[TreeNode]):
        nonlocal res
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    
    res = []
    dfs(root)
    return res

    