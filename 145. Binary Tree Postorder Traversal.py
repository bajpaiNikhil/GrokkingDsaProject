
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postOrder(treeNode):
    l = []

    def helper(Node):
        if Node is None:
            return
        helper(Node.left)
        helper(Node.right)
        l.append(Node.val)

    helper(treeNode)
    return l


treeNode = TreeNode(1)
treeNode.left = None
treeNode.right = TreeNode(2)
treeNode.right.left = TreeNode(3)
treeNode.right.right = None

print(postOrder(treeNode))
