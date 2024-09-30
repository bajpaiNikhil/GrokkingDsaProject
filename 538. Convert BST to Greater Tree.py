class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBSTtoGT(root):
    global sumis
    sumis = 0
    if root is None:
        return root

    def reverseInOrder(node):
        global sumis
        if node is None:
            return 0
        reverseInOrder(node.right)
        print(node, node.val)
        node.val = node.val + sumis
        sumis = node.val
        reverseInOrder(node.left)
        return node

    reverseInOrder(root)
    return root


treeNode = TreeNode(10)
treeNode.left = TreeNode(5)
treeNode.right = TreeNode(15)
treeNode.left.left = TreeNode(3)
treeNode.left.right = TreeNode(7)
treeNode.right.right = TreeNode(18)

print(convertBSTtoGT(treeNode))
