class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
def sumNumbers(root: Optional[TreeNode]) -> int:
    def dfs(root: TreeNode, num: str, res: List[int]):
        if root is None:
            return
                                
        if root.left is None and root.right is None:
            res.append(int(num + str(root.val)))
            return
        if root.left is not None:
            dfs(root.left, num + str(root.val), res)
        if root.right is not None:
            dfs(root.right, num + str(root.val), res)
                                
    res = []
    dfs(root, '', res)
    return sum(res)


root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
assert sumNumbers(root) == 1026