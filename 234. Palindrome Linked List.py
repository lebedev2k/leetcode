class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

def isPalindrome(head: Optional[ListNode]) -> bool:
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a == a[::-1]


r=isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
print(r)
r=isPalindrome(ListNode(1, ListNode(2)))
print(r)
    