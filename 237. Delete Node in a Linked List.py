class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(root, k):
    if root is None:
        return root
    head = root

    while head and head.next:
        if head.next.val == k:
            head.next = head.next.next
        head = head.next
    while root:
        print(root.val, end=" -> ")
        root = root.next
    return root


k = 5
ListNode1 = ListNode(4)
ListNode1.next = ListNode(5)
ListNode1.next.next = ListNode(1)
ListNode1.next.next.next = ListNode(9)
ListNode1.next.next.next.next = ListNode(6)
print(deleteNode(ListNode1, k))
