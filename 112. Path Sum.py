class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, targetSum):
        if not root: return False
        if not root.left and not root.right: return targetSum - root.val == 0
        if dfs(root.left, targetSum - root.val): return True
        if dfs(root.right, targetSum - root.val): return True
        return False
    if not root: return False
    return dfs(root, targetSum)


root = TreeNode(1, TreeNode(2))
print(hasPathSum(root, 1))

    
    