import collections
import queue
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


l = []


def findAllThePath(treeNode):
    pathList = []

    def helper(root, currentPath):
        if root is None:
            return
        currentPath.append(root.val)
        if root.left is None and root.right is None:
            a = ""
            for i in currentPath[:]:
                a += str(i) + "->"
            a = a[:-2]
            pathList.append(a)

        else:
            helper(root.left, currentPath[:])
            helper(root.right, currentPath[:])
        currentPath.pop()

    helper(treeNode, [])
    return pathList


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)

print(findAllThePath(treeNode))
