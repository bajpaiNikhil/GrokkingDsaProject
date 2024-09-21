class ListNode:

    def __init__(self, value=0, next=None):
        self.next = next
        self.val = value


def justPrintList(head,k):
    root = head
    curr, length = root, 0
    while curr:
        curr, length = curr.next, length + 1
    print(length)
    # Determine the length of each chunk
    chunk_size, longer_chunks = length // k, length % k
    res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
    print(chunk_size,longer_chunks,res)


ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(5)
ListNode1.next.next.next.next.next = ListNode(6)
ListNode1.next.next.next.next.next.next = ListNode(7)
ListNode1.next.next.next.next.next.next.next = ListNode(8)
ListNode1.next.next.next.next.next.next.next.next = ListNode(9)
ListNode1.next.next.next.next.next.next.next.next.next = ListNode(10)

print(justPrintList(ListNode1,3))
