class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


def addOneRow2(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    from collections import deque
    
    if depth == 1:
        return TreeNode(val, root)

    q_left = deque([root])    
    q_right = deque()
 
    cur_depth = 1
    while q_left or q_right:
        if  cur_depth+1 == depth:
            while q_left:
                node = q_left.popleft()
                node.left = TreeNode(val, left = node.left)# if node.left else None
                node.right = TreeNode(val, right = node.right)# if node.right else None
            while q_right:
                node = q_right.popleft()
                node.left = TreeNode(val, left = node.left)# if node.left else None
                node.right = TreeNode(val, right = node.right)# if node.right else None
        else:
            newlevel_left_nodes = deque()
            newlevel_right_nodes = deque()
            while q_left:
                node = q_left.popleft()
                if node.left:
                    newlevel_left_nodes.append(node.left)
                if node.right:
                    newlevel_right_nodes.append(node.right)
            while q_right:
                node = q_right.popleft()
                if node.left:
                    newlevel_left_nodes.append(node.left)
                if node.right:
                    newlevel_right_nodes.append(node.right)
            q_left = newlevel_left_nodes
            q_right = newlevel_right_nodes
            cur_depth += 1
            
    return root

        
def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    from collections import deque
    
    if depth == 1:
        return TreeNode(val, root)

    q = deque([root])    
 
    cur_depth = 1
    while q:
        if  cur_depth+1 == depth:
            while q:
                node = q.popleft()
                node.left = TreeNode(val, left = node.left)# if node.left else None
                node.right = TreeNode(val, right = node.right)# if node.right else None
        else:
            newlevel_nodes = deque()
            while q:
                node = q.popleft()
                if node.left:
                    newlevel_nodes.append(node.left)
            q = newlevel_nodes
            cur_depth += 1
            
    return root    


# root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
# newroot = addOneRow(root, 1, 2)
# print(newroot)

# root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
# newroot = addOneRow(root, 1, 3)
# print(newroot)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
newroot = addOneRow(root, 5, 4)
print(newroot)
        