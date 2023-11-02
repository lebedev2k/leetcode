#https://leetcode.com/problems/merge-two-sorted-lists/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1

    head = list2

    #previous_node = None
    current_node = list2
    while list1:
        #поиск подходящего места
        while current_node.next and list1.val > current_node.next.val:
            current_node = current_node.next

        tmp = list1
        list1 = list1.next

        if current_node == head:
            tmp.next = current_node
            head = tmp
        # elif not current_node.next:
        #     tmp.next = current_node.next
        #     current_node.next = tmp
        else:
            tmp.next = current_node.next
            current_node.next = tmp
        current_node = tmp

    return head


list1 = [1,2,4]
list2 = [1,3,4]

root1 = current_node = None
for item in list1:
    if current_node:
        current_node.next = ListNode(item)
        current_node = current_node.next
    else:
        root1 = current_node = ListNode(item)


root2 = current_node = None
for item in list2:
    if current_node:
        current_node.next = ListNode(item)
        current_node = current_node.next
    else:
        root2 = current_node = ListNode(item)

current_node = mergeTwoLists(root1, root2)
while current_node:
    print(current_node.val)
    current_node = current_node.next