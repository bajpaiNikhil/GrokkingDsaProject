import collections
import queue
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


l = []


def countNode(treeNode):
    count = 0
    l =[]
    def helper(node):
        if node is None:
            return
        l.append(1)
        helper(node.left)
        helper(node.right)


    helper(treeNode)
    return len(l)


treeNode = TreeNode(1)
treeNode.left = TreeNode(1)
treeNode.right = TreeNode(1)
treeNode.left.left = TreeNode(0)
treeNode.left.right = TreeNode(1)
treeNode.right.left = TreeNode(0)
treeNode.right.right = TreeNode(1)

print(countNode(treeNode))
