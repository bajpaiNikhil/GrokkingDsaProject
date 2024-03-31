class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def pairSum(listNode1):
    maxSum = 0
    slow = listNode1
    fast = listNode1
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # print(slow.val)
    current = slow.next
    slow.next= None
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    # print(prev.val)

    sumList1 = prev
    sumList2 = listNode1

    while sumList1 and sumList2:
        # print(sumList2.val,sumList1.val)
        maxSum= max(maxSum, sumList2.val+sumList1.val)
        sumList1 = sumList1.next
        sumList2 = sumList2.next
    print(maxSum)


ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(5)
ListNode1.next.next.next.next.next = ListNode(6)
ListNode1.next.next.next.next.next.next = ListNode(7)
ListNode1.next.next.next.next.next.next.next = ListNode(8)
ListNode1.next.next.next.next.next.next.next.next = ListNode(9)

print(pairSum(ListNode1))