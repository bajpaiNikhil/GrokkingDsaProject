from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    if root is None:
        return []
    q = deque([root])
    result = []
    while q:
        levelIs = len(q)
        averageAtLevel = []

        for i in range(levelIs):
            temp = q.popleft()
            averageAtLevel.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        result.append(sum(averageAtLevel) / len(averageAtLevel))
    return result


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)
print(averageOfLevels(treeNode))
