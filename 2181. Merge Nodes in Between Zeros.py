from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    empty_head = ListNode()
    last = empty_head
    head = head.next
    while head:
        summ = 0
        while head.val!= 0:
            summ += head.val
            head = head.next
        node = ListNode(summ)
        last.next = node
        last = node
        head = head.next
    return empty_head.next


n = mergeNodes(ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0)))))))))
print(n)
        
        


    


