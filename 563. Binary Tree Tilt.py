class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def findTilt(root: Optional[TreeNode]) -> int:
    ans = 0
    def dfs(root):
        nonlocal ans
        
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        ans += abs(left - right)
        return left + right + root.val
    dfs(root)
    return ans
                


root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, right=TreeNode(7)))
print(findTilt(root))