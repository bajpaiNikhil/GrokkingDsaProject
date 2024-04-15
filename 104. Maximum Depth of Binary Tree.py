
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depthOfTree(treeNode):
    if treeNode is None :
        return 0
    lst = depthOfTree(treeNode.left)
    rst = depthOfTree(treeNode.right)
    return 1+max(lst,rst)


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

print(depthOfTree(treeNode))
