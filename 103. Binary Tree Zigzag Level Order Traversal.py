import queue
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root):
    queue = deque([root])
    # q.append([root])
    l = []
    reverseOrder = True
    while queue:
        levelIs = len(queue)
        levelValue = []
        for i in range(levelIs):
            temp = queue.popleft()
            levelValue.append(temp.val)

            if reverseOrder:
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
            else:
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        # reverseOrder = not reverseOrder
        l.append(levelValue)
        reverseOrder = not reverseOrder
    return l


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

print(levelOrderTraversal(treeNode))
