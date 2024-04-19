from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or head.next is None:
        return head
    
    prev_node = head
    cur_node = head.next
    prev_node.next = None
    while cur_node:
        tmp = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = tmp
    
    return prev_node

root = reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(root)