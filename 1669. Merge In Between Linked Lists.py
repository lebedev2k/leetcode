class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    arr1 = []
    current_node = list1
    while current_node:
        arr1.append(current_node)
        current_node = current_node.next
    end_list2 = list2
    while end_list2.next:
        end_list2 = end_list2.next
    
    end_list2.next = arr1[b].next
    if a == 0:
        return list2
    else:
        arr1[a-1].next = list2
        return list1
    
        
    


head = mergeInBetween(ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5)))))), a=3, b=4, list2=ListNode(1000000, ListNode(1000001, ListNode(1000002))))
print(head)