from typing import List, Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        node = self
        while node:
            print(node.val, end=' ')
            node = node.next
            
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = head, head.next
        while node2:
            new_node = ListNode(math.gcd(node1.val, node2.val), node2)
            node1.next = new_node
            node1, node2 = node2, node2.next
        return head
            

root = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
root = Solution().insertGreatestCommonDivisors(root)
root.print()