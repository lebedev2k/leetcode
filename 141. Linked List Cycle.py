from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    cur_node = head
    while cur_node:
        cur_node.pos = 0
        cur_node = cur_node.next
        if hasattr(cur_node, 'pos'):
            return True
        
    return False


root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next = root.next
assert hasCycle(root) == True

root = ListNode(1)
root.next = ListNode(2)
root.next.next = root
assert hasCycle(root) == True   

root = ListNode(1)
assert hasCycle(root) == False   
