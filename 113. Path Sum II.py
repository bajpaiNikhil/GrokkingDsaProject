class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def pathWithSumFromRootToLeaf(treeNode):
#     paths = []
#
#     def helper(node, targetIs, currentSum, pathIs):
#
#         if node is None:
#             return False
#         pathIs.append(node.val)
#         currentSum += node.val
#         if node.left is None and node.right is None:
#
#             print(currentSum)
#             if currentSum == targetIs:
#                 paths.append(pathIs[:])
#
#         helper(node.left, targetIs, currentSum, pathIs[:])
#         helper(node.right, targetIs, currentSum, pathIs[:])
#
#     target = 18
#     helper(treeNode, target, 0, [])
#     return paths


def findAllPath(root,sumIs):
    paths = []

    def helper(node, sum, currentList, paths):
        if node is None:
            return
        currentList.append(node.val)
        if node.val == sum and node.left is None and node.right is None:
            paths.append(list(currentList))
        else:
            helper(node.left, sum - node.val, currentList, paths)
            helper(node.right, sum - node.val, currentList, paths)
        del currentList[-1]
    helper(root, sumIs , [], paths)
    return paths


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)

print(findAllPath(treeNode,18))
