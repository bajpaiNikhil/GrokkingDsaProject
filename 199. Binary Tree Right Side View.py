from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rhsForTree(root):
    if root is None:
        return []
    queue = deque([root])
    rhsList = []

    while queue:
        sizeOfQueue , rightMostVal = len(queue),0
        for i in range(sizeOfQueue):
            currentNode = queue.popleft()
            rightMostVal= currentNode.val
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        rhsList.append(rightMostVal)
    return rhsList


treeNode = TreeNode(6)
treeNode.left = TreeNode(2)
treeNode.left.left = TreeNode(0)
treeNode.left.right = TreeNode(4)
treeNode.left.right.left = TreeNode(3)
treeNode.left.right.right = TreeNode(5)
treeNode.right = TreeNode(8)
treeNode.right.left = TreeNode(7)
treeNode.right.right = TreeNode(9)

print(rhsForTree(treeNode))
