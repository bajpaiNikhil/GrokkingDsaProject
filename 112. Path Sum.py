class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumRootToLeaf(treeNode):
    def helper(node, targetIs, currentSum):

        if node is None:
            return False
        # pathIs.append(node.val)
        currentSum += node.val
        if node.left is None and node.right is None:
            # paths.append(sum(pathIs[:]))
            print(currentSum)
            return currentSum == targetIs

        l = helper(node.left, targetIs, currentSum)
        r = helper(node.right, targetIs, currentSum)
        return l or r

    target = 189
    return helper(treeNode, target, 0)


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)

print(sumRootToLeaf(treeNode))
