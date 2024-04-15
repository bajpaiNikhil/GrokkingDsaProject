class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathWithSumFromRootToLeaf(treeNode):
    paths= []
    def helper(node, targetIs, currentSum,pathIs):

        if node is None:
            return False
        pathIs.append(node.val)
        currentSum += node.val
        if node.left is None and node.right is None:

            print(currentSum)
            if currentSum == targetIs:
                paths.append(pathIs[:])

        l = helper(node.left, targetIs, currentSum,pathIs[:])
        r = helper(node.right, targetIs, currentSum,pathIs[:])

    target = 18
    helper(treeNode, target, 0,[])
    return paths


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)

print(pathWithSumFromRootToLeaf(treeNode))
