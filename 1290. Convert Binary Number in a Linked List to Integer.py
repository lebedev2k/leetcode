class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
    res = 0
    while head:
        res = (res << 1) + head.val
        head = head.next        
    return res

print(getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))
