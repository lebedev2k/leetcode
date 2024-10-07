class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        prev_node = node
        while node.next:
            node.val = node.next.val
            prev_node = node
            node = node.next
        prev_node.next = None
        
    
    
root = ListNode(4)
root.next = ListNode(5)
root.next.next = ListNode(1)
root.next.next.next = ListNode(9)

Solution().deleteNode(root.next)
print(root)