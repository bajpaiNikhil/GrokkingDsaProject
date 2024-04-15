class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumRootToLeaf(treeNode):
    # pathIs = []
    #
    # def helper(node, pathSumIs):
    #     if node is None:
    #         return
    #     pathSumIs.append(node.val)
    #     if node.left is None and node.right is None:
    #         pathIs.append(int(''.join(map(str, pathSumIs[:]))))
    #     else:
    #         helper(node.left, pathSumIs[:])
    #         helper(node.right, pathSumIs[:])
    #     pathSumIs.pop()
    #
    # helper(treeNode, [])
    # return sum(pathIs)
    def helper(node, current_sum):
        if node is None:
            return 0

        # Calculate the new sum by shifting the current sum left and adding the current node value
        new_sum = (current_sum * 10) + node.val

        # If it's a leaf node, return the new sum
        if node.left is None and node.right is None:
            return new_sum

        # Otherwise, recursively process left and right subtrees
        left_sum = helper(node.left, new_sum)
        right_sum = helper(node.right, new_sum)

        return left_sum + right_sum
    return helper(treeNode,0)


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)

print(sumRootToLeaf(treeNode))
