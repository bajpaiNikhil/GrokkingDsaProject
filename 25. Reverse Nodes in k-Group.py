class ListNode:

    def __init__(self, value=0, next=None):
        self.next = next
        self.val = value


def reverseLinkedList(nextNode, k):
    currentNode = nextNode
    prev = None

    for _ in range(k):
        nextIs = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = nextIs
    return prev,currentNode


def reverseInKGroup(head, k):
    dummyNode = ListNode(0)
    dummyNode.next = head
    prt = dummyNode

    while prt is not None:
        tracker = prt

        for i in range(k):
            if not tracker:
                break
            tracker = tracker.next
        if tracker is None:
            break
        updatedNodes = reverseLinkedList(prt.next, k)
        previous, current = updatedNodes[0], updatedNodes[1]

        lastNodeOfReversedGroup =prt.next
        lastNodeOfReversedGroup.next = current
        prt.next = previous
        prt = lastNodeOfReversedGroup
    return dummyNode.next


ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(5)
ListNode1.next.next.next.next.next = ListNode(6)
ListNode1.next.next.next.next.next.next = ListNode(7)
ListNode1.next.next.next.next.next.next.next = ListNode(8)
ListNode1.next.next.next.next.next.next.next.next = ListNode(9)
