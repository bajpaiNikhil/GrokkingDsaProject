class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = []


def rangeSumBST(root, low, right):
    if root is None:
        return 0
    sum = 0
    if root.val > low:
        sum += rangeSumBST(root.left, low, right)
    if root.val < right:
        sum += rangeSumBST(root.right, low, right)
    if low <= root.val <= right:
        sum += root.val
    return sum


treeNode = TreeNode(10)
treeNode.left = TreeNode(5)
treeNode.right = TreeNode(15)
treeNode.left.left = TreeNode(3)
treeNode.left.right = TreeNode(7)
treeNode.right.right = TreeNode(18)
low = 7
high = 15

print(rangeSumBST(treeNode,low ,high))
