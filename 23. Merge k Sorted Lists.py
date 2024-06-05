import heapq


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def mergeKList(lists):
    minHeap = []
    head = ListNode(None)
    current = head

    for i in range(len(lists)):
        print(lists[i])
        if lists[i]:
            heapq.heappush(minHeap,(lists[i].val,i))
            lists[i] = lists[i].next
    print(minHeap)

    while minHeap:
        val , i = heapq.heappop(minHeap)
        current.next = ListNode(val)
        current = current.next
        if lists[i]:
            heapq.heappush(minHeap,(lists[i].val,i))
            lists[i] = lists[i].next
    return head.next
l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

print(mergeKList([l1, l2, l3]))
