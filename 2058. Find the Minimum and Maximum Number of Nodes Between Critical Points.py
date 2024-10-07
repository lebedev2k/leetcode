class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
    critical_points = []
    num = 0
    while head.next and head.next.next:
        if (head.val>head.next.val<head.next.next.val) or (head.val<head.next.val>head.next.next.val):
            critical_points.append(num)
        head = head.next
        num += 1

    minDistance = min([critical_points[i+1] - critical_points[i] for i in range(len(critical_points)-1)]) if len(critical_points)>1 else -1 
    maxDistance = critical_points[-1] - critical_points[0] if len(critical_points)>1 else -1
    # print(critical_points)  
    # print([minDistance, maxDistance])
    return [minDistance, maxDistance]

root = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
assert nodesBetweenCriticalPoints(root) == [1,3]