class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional    
def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:
    from collections import deque
    node = head
    stack = deque()
    while node:
        stack.append(node)
        node = node.next
    
    e = 0
    while stack:
        node = stack.pop()        
        e, node.val = divmod(node.val*2 + e, 10)
    if e: return ListNode(e, head)
    return head
                
                


res = doubleIt(ListNode(1, ListNode(8, ListNode(9))))
print(res)
res = doubleIt(ListNode(9, ListNode(9, ListNode(9))))
print(res)
res = doubleIt(ListNode(9))
print(res)