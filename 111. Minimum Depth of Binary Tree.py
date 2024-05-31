from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depthOfTree(root):
    if root is None:
        return []
    minimumDepthIs = 0
    q = deque([root])
    while q:
        minimumDepthIs+=1
        levelIs = len(q)
        for i in range(levelIs):
            temp = q.popleft()
            # The only difference will be, instead of keeping track of all the nodes in a level, we will only track
            # the depth of the tree. As soon as we find our first leaf node, that level will represent the minimum
            # depth of the tree.
            if not temp.left and not temp.right:
                return minimumDepthIs
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
#
# def depthOfTree(treeNode):
#     isDepth = []
#     def helperDepth(node , depth , path):
#
#         if node is None :
#             return 0
#         depth+=1
#         if node.left is None and node.right is None :
#             path.append(depth)
#         helperDepth(node.left,depth,path)
#         helperDepth(node.right,depth, path)
#         return path
#     helperDepth(treeNode,0,isDepth)
#     return isDepth




treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)
print(depthOfTree(treeNode))
