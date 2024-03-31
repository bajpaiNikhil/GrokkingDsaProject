
class Node:

    def __init__(self, value = 0 , next = None):
        self.next = next
        self.value = value



def mergeTwoSortedList(head1, head2):

    dummyNode = Node(-1)
    tail = dummyNode
    while head1 is not None and head2 is not None:
        if head1.value < head2.value:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
            tail.next = None
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next
            tail.next = None
    return dummyNode.next



Head1 = Node(1)
Head1.next = Node(2)
Head1.next.next = Node(4)


Head2 = Node(1)
Head2.next = Node(3)
Head2.next.next = Node(4)

print(mergeTwoSortedList(Head1,Head2))