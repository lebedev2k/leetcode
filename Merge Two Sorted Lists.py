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

    current_node = list2

    while list1: #берем поочереди элементы из списка 1 и ищем куда их вставить в список 2
        #поиск подходящего места для вставки
        while current_node.next and list1.val > current_node.next.val:
            current_node = current_node.next

        tmp = list1
        list1 = list1.next

        if current_node == head: #найденное место совпадает с головой списка, в который вставляем
            if current_node.val > tmp.val: #определяем вставлять до или после головы
                tmp.next = current_node
                head = tmp #вставили в начало списка, поэтому меняется голова
            else:
                tmp.next = current_node.next
                current_node.next = tmp
        else:
            tmp.next = current_node.next
            current_node.next = tmp
        current_node = tmp

    return head


list1 = [1,2,3]
list2 = [2,5,8]

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

"""
Хорошее решение

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next 
"""