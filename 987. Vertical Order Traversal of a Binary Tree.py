import collections
import queue
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrderTraversal(root):
    q = deque([(root, 0)])
    l = []
    mHashMap = {}
    maxL = 0
    minL = 0
    while q:
        levelIs = len(q)
        for i in range(levelIs):
            temp = q.popleft()
            current = temp[0]
            level = temp[1]
            if level not in mHashMap:
                mHashMap[level] = []
            mHashMap[level] += [current.val]
            maxL = max(maxL, level)
            minL = min(minL, level)
            if current.left:
                q.append((current.left, level - 1))
            if current.right:
                q.append((current.right, level + 1))
    print(maxL, minL, mHashMap)
    for i in range(minL, maxL + 1):
        l.append(mHashMap[i])
    return l


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)
treeNode.left.left = TreeNode(4)
treeNode.left.right = TreeNode(5)
treeNode.right.left = TreeNode(6)
treeNode.right.right = TreeNode(7)

print(levelOrderTraversal(treeNode))
k = levelOrderTraversal(treeNode)
