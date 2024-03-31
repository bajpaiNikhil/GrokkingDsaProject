
class Node:

    def __init__(self, value = 0 , next = None):
        self.next = next
        self.val = value

def addTwoNumbers(l1,l2):
    dummy = Node(0)
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        value1 = l1.val if l1 else 0
        value2 = l2.val if l2 else 0

        value12 = value1 + value2 + carry
        carry = value12 // 10
        valueToAdd = value12 % 10

        current.next = Node(valueToAdd)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


Head1 = Node(1)
Head1.next = Node(2)
Head1.next.next = Node(4)


Head2 = Node(1)
Head2.next = Node(3)
Head2.next.next = Node(4)
print(addTwoNumbers(Head1,Head2))