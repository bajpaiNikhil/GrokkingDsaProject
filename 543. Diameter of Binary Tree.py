
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfTree(treeNode):

    def depth(node):
        if node is None :
            return 0
        return 1+max(depth(node.left),depth(node.right))
    return depth(treeNode.left)+depth(treeNode.right)



treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

print(diameterOfTree(treeNode))
