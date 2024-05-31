class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def sumRootToLeaf(treeNode):
#     def helper(node, targetIs, currentSum):
#
#         if node is None:
#             return False
#         # pathIs.append(node.val)
#         currentSum += node.val
#         if node.left is None and node.right is None:
#             # paths.append(sum(pathIs[:]))
#             print(currentSum)
#             return currentSum == targetIs
#
#         l = helper(node.left, targetIs, currentSum)
#         r = helper(node.right, targetIs, currentSum)
#         return l or r
#
#     target = 189
#     return helper(treeNode, target, 0)

def sumRootToLeaf(root,sum):
    if root is None: return False

    if root.val == sum and root.left is None and root.right is None:
        return True
    else:
        return sumRootToLeaf(root.left , sum-root.val) or sumRootToLeaf(root.right , sum-root.val)


treeNode = TreeNode(4)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(0)
treeNode.left.left = TreeNode(5)
treeNode.left.right = TreeNode(1)
sumis = 14
print(sumRootToLeaf(treeNode,sumis))
