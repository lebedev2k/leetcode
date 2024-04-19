class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    
    prev_node = head
    cur_node = head.next
    while cur_node:
        if cur_node.val == prev_node.val:
            prev_node.next = cur_node.next
        else:
            prev_node = cur_node
        cur_node = cur_node.next
    return head

def createLinkedList(values: List[int])->ListNode:
    if not values:
        return None
    
    root = ListNode(values[0])
    current_node = root
    for i in range(1, len(values)):
        node = ListNode(values[i])
        current_node.next = node
        current_node = node
    return root

root = createLinkedList([1,1,2])

deleteDuplicates(root)
