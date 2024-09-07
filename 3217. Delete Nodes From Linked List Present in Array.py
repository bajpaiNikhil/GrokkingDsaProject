class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(5)
nums = [1, 2, 3]

numsSet = set(nums)

while ListNode1.val in numsSet:
    ListNode1 = ListNode1.next
ans = ListNode(ListNode1.val, ListNode1)

while ListNode1 and ListNode1.next:
    if ListNode1.val in numsSet:
        ListNode1.next = ListNode1.next.next
    else:
        ListNode1 = ListNode1.next
print(ans.next)