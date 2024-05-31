from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if root is None:
        return []
    q = deque([root])
    while q :
        previousNode = None
        temp = q.popleft()
        levelIs = len(q)
        for i in range(levelIs):
            temp = q.popleft()
            if previousNode:
                previousNode.next = temp
            previousNode = temp
            if temp.left :
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)



treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)