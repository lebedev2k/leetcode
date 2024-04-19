class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def reorderList(head: Optional[ListNode]) -> None:
    if not head.next:
        return
    cur_node = head
    a = []
    while cur_node:
        a.append(cur_node)
        cur_node = cur_node.next
    i, j = 1, len(a)-1
    cur_node = a[0]
    while i<j:
        cur_node.next = a[j]
        cur_node = cur_node.next        
        cur_node.next = a[i]
        cur_node = cur_node.next        
        i += 1 
        j -= 1
    if len(a)%2 == 0:
        cur_node.next = a[i]
        cur_node.next.next = None
    else:
        cur_node.next = None
        

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(head)
print(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorderList(head)
print(head)