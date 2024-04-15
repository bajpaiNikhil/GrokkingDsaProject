
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def pathSumBetweenAnyTwoNode(root):
    globalVariableMaxPathSum = float('-inf')

    def helper(node):
        if node is None:
            return 0
        l = helper(node.left)
        r = helper(node.right)
        nonlocal globalVariableMaxPathSum
        print(node.val+max(l,0)+max(r,0) ,l,r,node.val)
        globalVariableMaxPathSum = max(globalVariableMaxPathSum, node.val + l + r)
        return node.val + (max(l, r, 0))

    helper(treeNode)
    return 837202734092
    # paths = []
    # def helper(node, targetIs, currentSum, pathIs):
    #     if node is None:
    #         return False
    #     pathIs.append(node.val)
    #     currentSum += node.val
    #     print(currentSum)
    #     if currentSum == targetIs:
    #         paths.append(pathIs[:])
    #     helper(node.left, targetIs, currentSum, pathIs[:])
    #     helper(node.right, targetIs, currentSum, pathIs[:])
    # target = 21
    # helper(root, target, 0, [])
    # return paths

treeNode = TreeNode(10)
treeNode.left = TreeNode(7)
treeNode.right = TreeNode(-3)
treeNode.left.left = TreeNode(3)
treeNode.left.left.left = TreeNode(3)
treeNode.left.left.right = TreeNode(2)
treeNode.left.right = TreeNode(2)
treeNode.left.right.right = TreeNode(1)
treeNode.right.right = TreeNode(11)
print(pathSumBetweenAnyTwoNode(treeNode))