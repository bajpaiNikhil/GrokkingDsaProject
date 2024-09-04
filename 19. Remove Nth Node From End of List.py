class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(listNode1, k):
    left = listNode1
    right = listNode1
    n = k
    for i in range(k):
        right = right.next
    if right is None:
        return listNode1.next

    while right.next is not None:
        left = left.next
        right = right.next

    left.next = left.next.next
    return listNode1

    # size = 0
    # temp = listNode1
    # head = listNode1
    #
    # while temp:
    #     size += 1
    #     temp = temp.next
    # if size == 1:
    #     return ListNode(0).next
    # elementToDeleteFromStart = size - k
    # while head:
    #     if elementToDeleteFromStart == 1:
    #         head.next = head.next.next
    #     if elementToDeleteFromStart == 0:
    #         head = head.next
    #     else:
    #         elementToDeleteFromStart -= 1
    #         head = head.next
    # while listNode1:
    #     print(listNode1.val)
    #     listNode1 = listNode1.next
    # return head


k = 2
ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
# ListNode1.next.next = ListNode(3)
# ListNode1.next.next.next = ListNode(4)
# ListNode1.next.next.next.next = ListNode(5)
print(removeNthFromEnd(ListNode1, 2))
