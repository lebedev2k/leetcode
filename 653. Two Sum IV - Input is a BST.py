class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import defaultdict
from typing import Optional


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    def dfs(root: Optional[TreeNode]):
        if not root:
            return         
        dfs(root.left)
        dfs(root.right)
        h[root.val] += 1
    h = defaultdict(int)
    dfs(root)
    for val in h.keys():
        if (k - val) == val:
            if h[val] > 1:
                return True
            else:
                continue
        if (k - val ) in h:
            return True
    return False


root = TreeNode(1)
assert findTarget(root, 2) == False

root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, right=TreeNode(7)))
assert findTarget(root, 9) == True

root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, right=TreeNode(7)))
assert findTarget(root, 28) == False
