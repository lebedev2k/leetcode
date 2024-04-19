from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    n = 0
    cur_node = head
    while cur_node:
        cur_node = cur_node.next
        n += 1
    n = n//2
    cur_node = head
    for i in range(n):
        cur_node = cur_node.next
    return cur_node
    


def createLinkedList(nums):
    root = cur_node = None
    for n in nums:
        if not root:
            root = cur_node = ListNode(n)
        else:
            cur_node.next = ListNode(n)
            cur_node = cur_node.next
            
    return root 


assert middleNode(createLinkedList([1,2,3,4,5])).val == 3
assert middleNode(createLinkedList([1,2,3,4,5,6])).val == 4
