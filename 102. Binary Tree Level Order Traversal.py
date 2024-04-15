import queue
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root):
    q = deque([root])
    # q.append([root])
    l = []
    while q:
        levelIs = len(q)
        levelValue = []
        for i in range(levelIs):
            temp = q.popleft()
            levelValue.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        l.append(levelValue)
    return l


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

print(levelOrderTraversal(treeNode))
