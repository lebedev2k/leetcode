class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    def dfs(root: TreeNode, level: int, isleft: bool, nodes: list[tuple[int, int]], nodesr: list[tuple[int, int]], n: int):
        if not root:
            return n
        
        # print(root.val, level, n)
        n -= 1
        if isleft and not root.left:
            nodes.append((level, n, root.val))
        if not isleft and not root.right:
            nodesr.append((level, n, root.val))
            
        n = dfs(root.left, level+1, True, nodes, nodesr, n)
        n = dfs(root.right, level+1, False, nodes, nodesr, n)
        return n

    nodes =[]
    nodesr =[]
    dfs(root,0, False, nodes, nodesr, 10000)
    if nodes:
        nodes.sort(reverse=True)
        return nodes[0][2]
    else:
        nodesr.sort(reverse=True)
        return nodesr[0][2]


root = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
assert findBottomLeftValue(root) == 0

root = TreeNode(0, right = TreeNode(-1))
assert findBottomLeftValue(root) == -1

root = TreeNode(0)
assert findBottomLeftValue(root) == 0

root = TreeNode(2, TreeNode(1), TreeNode(3))
assert findBottomLeftValue(root) == 1

root = TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3, TreeNode(5, left=TreeNode(7)), TreeNode(6)))
assert findBottomLeftValue(root) == 7
