


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverseTree(treeNode):
    l = []

    if treeNode is None:
        return
    left = reverseTree(treeNode.left)
    right = reverseTree(treeNode.right)

    treeNode.left = right
    treeNode.right = left
    return treeNode


def print_tree_inorder(treeNode):
    if treeNode:
        print_tree_inorder(treeNode.left)
        print(treeNode.val, end=" ")  # Print the value
        print_tree_inorder(treeNode.right)


treeNode = TreeNode(2)
treeNode.left = TreeNode(1)
treeNode.right = TreeNode(3)

print(print_tree_inorder(treeNode))
k = reverseTree(treeNode)

print(print_tree_inorder(k))
