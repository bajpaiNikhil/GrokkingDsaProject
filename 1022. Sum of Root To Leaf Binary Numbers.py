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

    def helper(node, current_path):
        if not node:
            return
        current_path.append(node.val)
        if node.left is None and node.right is None:
            # Calculate the binary value of the path
            binary_value = int(''.join(map(str, current_path)), 2)
            print(binary_value , current_path)
            pathList.append(binary_value)
        else:
            helper(node.left, current_path[:])  # Pass a copy of the current path
            helper(node.right, current_path[:])
        # Backtrack: remove the last element (current node) from the path
        current_path.pop()

    helper(treeNode, [])
    return sum(pathList)


treeNode = TreeNode(1)
treeNode.left = TreeNode(1)
treeNode.right = TreeNode(1)
treeNode.left.left = TreeNode(0)
treeNode.left.right = TreeNode(1)
treeNode.right.left = TreeNode(0)
treeNode.right.right = TreeNode(1)

print(findAllThePath(treeNode))
