from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque 

class Solution:
    # def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     q = deque()
    #     if root.right: q.append(root.right)
    #     q.append(root)
    #     if root.left: q.append(root.left)
    #     while q:
    #         l, r = q.pop(), q.pop()
    #         if l.left is None and l.right is None:
    #             res.append(l.val)
    #         if r.left is None and r.right is None:
    #             res.append(r.val)
    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, res: List[int]):
            if node is None: return 
            dfs(node.left, res)
            dfs(node.right, res)
            res.append(node.val)
        dfs(root, res)
        return res
        
        