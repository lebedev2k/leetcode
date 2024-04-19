class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

def isSameTree2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return str(p) == str(q)


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    from collections import deque
    if (not p and not q):
        return True
    if (p and not q) or (q and not p):
        return False

    q1 = deque()
    q2 = deque()
    if p.val == q.val:
        q1.append(p)
        q2.append(q)
    else:
        return False
    while q1 and q2:
        node1 = q1.popleft()
        node2 = q2.popleft()
        if node1.left and node2.left and node1.left.val == node2.left.val:
            q1.append(node1.left)
            q2.append(node2.left)
        elif node1.left and node2.left and node1.left.val != node2.left.val:
            return False
        elif any ([node1.left,node2.left]):
            return False

        if node1.right and node2.right and node1.right.val == node2.right.val:
            q1.append(node1.right)
            q2.append(node2.right)
        elif node1.right and node2.right and node1.right.val != node2.right.val:
            return False
        elif any([node1.right,node2.right]):
            return False
        
    return True        
    
        

root1 = TreeNode(0)
root2 = TreeNode(1)
assert isSameTree2(root1, root2) == False


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
assert isSameTree2(root1, root2) == True

root1 = TreeNode(1, left=TreeNode(2))
root2 = TreeNode(1, right=TreeNode(2))
assert isSameTree2(root1, root2) == False


root1 = TreeNode(1, TreeNode(2), TreeNode(1))
root2 = TreeNode(1, TreeNode(1), TreeNode(2))
assert isSameTree(root1, root2) == False
