# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        root: ListNode = head
        while root:
            N += 1
            root = root.next
        n, r = divmod(N, k)
        res = []
        for _ in range(k):
            part_root = head
            d = 1 if r>0 else 0
            if part_root:
                part_end = None
                for _ in range(n+d):
                    part_end = head
                    head = head.next
                part_end.next = None
            r = max(r-1, 0)
            res.append(part_root)
        return res
        
    
assert Solution().splitListToParts(ListNode(1, ListNode(2, ListNode(3))), 5) == [[1], [2], [3], [], []]

  