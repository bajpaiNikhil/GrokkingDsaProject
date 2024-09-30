from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root):
    queue = deque([(root, 0)])
    max_width = 0
    while queue:
        levelLength = len(queue)
        _, levelStart = queue[0]
        print(_.val, levelStart, levelLength)
        for level in range(levelLength):
            node,index = queue.popleft()
            if node.left:
                queue.append((node.left,2*index))
            if node.right:
                queue.append((node.right,2*index+1))

            max_width = max(max_width,index-levelStart+1)
    return max_width



treeNode = TreeNode(6)
treeNode.left = TreeNode(2)
treeNode.left.left = TreeNode(0)
# treeNode.left.right = TreeNode(4)
# treeNode.left.right.left = TreeNode(3)
# treeNode.left.right.right = TreeNode(5)
treeNode.right = TreeNode(8)
# treeNode.right.left = TreeNode(7)
# treeNode.right.right = TreeNode(9)
print(widthOfBinaryTree(treeNode))
