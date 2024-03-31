

class ListNode:

    def __init__(self, value = 0 , next = None):
        self.next = next
        self.val = value


def rotateBetweenTwoPoints(head1,left , right ):

    dummyNode = ListNode(0)
    dummyNode.next = head1
    temp1 = dummyNode
    count = 0
    while count < left-1:
        count+=1
        temp1 = temp1.next
        # print(temp1.val)

    reversePoint =None
    current = temp1.next
    while right>=left :
        nxt = current.next
        current.next = reversePoint
        reversePoint = current
        current = nxt

        right-=1
    temp1.next.next = current
    temp1.next = reversePoint
    # print(current.val)
    # print(temp1.next.val)
    # # print(temp1.next.next.val)
    # print(reversePoint.val)
    k  = dummyNode
    while k:
        print(k.val)
        k = k.next
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
left = 4
right = 7

print(rotateBetweenTwoPoints(ListNode1,left,right))