from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
#     if root is None:
#         return 0
#     if root.left and not root.left.left:
#         return root.left.val
    
#     return sumOfLeftLeaves(root.left)+sumOfLeftLeaves(root.right)

def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    from collections import deque
    q = deque()
    q.append(root)
    summ = 0
    while q:
        node = q.pop()
        if node.left and node.left.left is None and node.left.right is None:
            summ += node.left.val
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return summ


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
res = sumOfLeftLeaves(root)
print(res)
assert  res == 24

root = TreeNode(0, TreeNode(2, TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(1)), TreeNode(-1, right=TreeNode(6, right=TreeNode(8))))), TreeNode(4))
res = sumOfLeftLeaves(root)
print(res)
assert  res == 5