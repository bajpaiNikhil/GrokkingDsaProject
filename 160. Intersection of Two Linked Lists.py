class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def intersectionOfLL(headA, headB):
    if headA is None or headB is None:
        return []
    mHashSet = set()

    aHead = headA
    bHead = headB
    while aHead != bHead:

        if aHead is None:
            aHead = headB
        else:
            aHead = aHead.next
        if bHead is None:
            bHead = headA
        else:
            bHead = bHead.next
    return aHead.val


ListNode1 = ListNode(4)
ListNode1.next = ListNode(1)
ListNode1.next.next = ListNode(8)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(77)

ListNode2 = ListNode(6)
ListNode2.next = ListNode1.next.next

print(intersectionOfLL(ListNode1, ListNode2))
