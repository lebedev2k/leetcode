class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
def sumNumbers(root: Optional[TreeNode]) -> int:
    def dfs(root: TreeNode, num: str, res: List[str]):
        if root is None:
            return
                                
        if root.left is None and root.right is None:
            res.append(string.ascii_lowercase[root.val]+num)
            return
        if root.left is not None:
            dfs(root.left, string.ascii_lowercase[root.val]+num, res)
        if root.right is not None:
            dfs(root.right, string.ascii_lowercase[root.val]+num, res)
    
    import string
    
    res = []
    dfs(root, '', res)
    res.sort()
    return res[0]


root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
assert sumNumbers(root) == 1026