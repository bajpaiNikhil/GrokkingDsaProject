
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depthOfTree(treeNode):
    isDepth = []
    def helperDepth(node , depth , path):

        if node is None :
            return 0
        depth+=1
        if node.left is None and node.right is None :
            path.append(depth)
        helperDepth(node.left,depth,path)
        helperDepth(node.right,depth, path)
        return path
    helperDepth(treeNode,0,isDepth)
    return isDepth




treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)
print(depthOfTree(treeNode))
