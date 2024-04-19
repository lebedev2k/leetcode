class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur_node = prev_node = head
    a = []
    while cur_node:
        a.append(cur_node)
        cur_node = cur_node.next
    n = len(a) - n
    if n == 0:
        return a[n].next
    else:
        a[n-1].next = a[n+1]
        return head
        

# def makeLinkedList(values: List[int]):
    
answer = removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
answer = removeNthFromEnd(ListNode(1), 1)
answer = removeNthFromEnd(ListNode(1, ListNode(2)), 1)
# assert removeNthFromEnd(makeLinkedList([1,2,3,4,5]), 2) == 