class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubPath(root, head):
    subPath = ""
    delimeter = ","
    while head:
        subPath += str(head.val) + delimeter
        head = head.next
    print(subPath)

    def dfs(root, path):
        if subPath in path:
            return True
        if not root:
            return False
        else:
            return dfs(root.left, path + str(root.val) + delimeter) or dfs(root.right, path + str(root.val) + delimeter)

    return dfs(root, "")


ListNode1 = ListNode(1)
ListNode1.next = ListNode(2)
ListNode1.next.next = ListNode(3)

treeNode = TreeNode(1)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(2)
treeNode.right.left = TreeNode(2)
treeNode.right.right = TreeNode(7)

print(isSubPath(treeNode, ListNode1))
