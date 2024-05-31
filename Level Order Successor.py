from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderSuccessor(root, currentNode):
    if root is None:
        return None
    q = deque([root])
    result = []
    while q:
        temp = q.popleft()
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

        if currentNode == temp.val:
            break
    return q[0] if q else None


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)
currentNode = 15

print(levelOrderSuccessor(treeNode,currentNode))
