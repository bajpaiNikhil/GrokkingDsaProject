import math
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumEvenGrandParentsUsingLevelOrderTraversal(treeNode):

    queue = deque([(treeNode, -1)])
    result = 0
    while queue:
        node , parentValue = queue.popleft()
        for child in node.left,node.right:
            if child:
                if parentValue%2 == 0:
                    result+=child.val
                queue.append((child,node.val))
    return result


treeNode = TreeNode(6)
treeNode.left = TreeNode(7)
treeNode.right = TreeNode(8)
treeNode.left.left = TreeNode(2)
treeNode.left.left.left = TreeNode(9)
treeNode.left.right = TreeNode(7)
treeNode.left.right.left = TreeNode(1)
treeNode.left.right.right = TreeNode(4)
treeNode.right.left = TreeNode(1)
treeNode.right.right = TreeNode(3)
treeNode.right.right.right = TreeNode(5)
print(sumEvenGrandParentsUsingLevelOrderTraversal(treeNode))