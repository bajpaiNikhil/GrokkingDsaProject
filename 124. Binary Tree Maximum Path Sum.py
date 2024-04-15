
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSumBinaryTree(treeNode):
    globalVariableMaxPathSum = float('-inf')

    def helper(node):
        if node is None:
            return 0
        l = helper(node.left)
        r = helper(node.right)
        nonlocal globalVariableMaxPathSum

        globalVariableMaxPathSum = max(globalVariableMaxPathSum, node.val + l + r)
        return node.val + (max(l,r,0))
    helper(treeNode)
    return globalVariableMaxPathSum


treeNode = TreeNode(1)
treeNode.left = TreeNode(2)
treeNode.right = TreeNode(3)

print(maxPathSumBinaryTree(treeNode))
