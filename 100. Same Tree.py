
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sameTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    else:
        leftSubTree = sameTree(root1.left,root2.left)
        rightSubTree = sameTree(root1.right,root2.right)
        return leftSubTree and rightSubTree



treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(204)

treeNode2 = TreeNode(3)
treeNode2.left = TreeNode(9)
treeNode2.right = TreeNode(20)
print(sameTree(treeNode,treeNode2))