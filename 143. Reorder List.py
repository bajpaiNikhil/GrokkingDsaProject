class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reorderLL(head):
    if not head: return []
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # step 2: reverse second half
    prev, curr = None, slow.next
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    slow.next = None

    # step 3: merge lists
    head1 = head
    head2 = prev

    while head1 and head2:
        nxt1 = head1.next
        nxt2 = head2.next

        head1.next = head2
        head1 = nxt1

        head2.next = head1
        head2 = nxt2
    return head


ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)
ListNode1.next.next.next = ListNode(4)
ListNode1.next.next.next.next = ListNode(5)
ListNode1.next.next.next.next.next = ListNode(6)
ListNode1.next.next.next.next.next.next = ListNode(7)
ListNode1.next.next.next.next.next.next.next = ListNode(8)
ListNode1.next.next.next.next.next.next.next.next = ListNode(9)

# print(reorderLL(ListNode1))
reversed_list = reorderLL(ListNode1)
while reversed_list:
    print(reversed_list.val, end=" -> ")
    reversed_list = reversed_list.next
# print(findMiddle(ListNode1))
# print(reverseLL(ListNode1))
# reversed_list = reverseLL(ListNode1)

# Print the reversed list (values)
# while reversed_list:
#     print(reversed_list.val, end=" -> ")
#     reversed_list = reversed_list.next

# k = reverseLL(ListNode1)
# while k:
#     print(k.val , end= "->")
#     k = k.next


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def reverseLL(head):
#     current = head
#     prev = None
#     while current:
#         nxt = current.next
#         current.next = prev
#         prev = current
#         current = nxt
#
#     # Update the head pointer to the new head (prev)
#     head = prev
#
#     return head
#
#
# # Example usage:
# # Create a linked list (you can replace this with your own list)
# listA = ListNode(1)
# listA.next = ListNode(2)
# listA.next.next = ListNode(3)
#
# reversed_list = reverseLL(listA)
#
# # Print the reversed list (values)
# while reversed_list:
#     print(reversed_list.val, end=" -> ")
#     reversed_list = reversed_list.next
