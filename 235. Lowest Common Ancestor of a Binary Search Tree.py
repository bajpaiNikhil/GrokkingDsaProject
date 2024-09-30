class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


treeNode = TreeNode(6)
treeNode.left = TreeNode(2)
treeNode.left.left = TreeNode(0)
treeNode.left.right = TreeNode(4)
treeNode.left.right.left = TreeNode(3)
treeNode.left.right.right = TreeNode(5)
treeNode.right = TreeNode(8)
treeNode.right.left = TreeNode(7)
treeNode.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(4)


def lowestCommonAncestor(root, p, q):
    while root:
        if root is None:
            return []
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root.val



# def lowestCommonAncestor(root, p, q):
#     list1 = []
#     list2 = []
#
#     def searchInBst(root, node,path):
#         if root is None:
#             return []
#         path.append(root.val)
#         if root.val > node.val:
#             searchInBst(root.left, node, path)
#         elif root.val < node.val:
#             searchInBst(root.right, node, path)
#         else:
#             return path
#
#     searchInBst(root, p,list1)
#     searchInBst(root, q,list2)
#     print(list1,list2)
#     common_elements = list(filter(lambda x: x in list2, list1))
#     return common_elements


print(lowestCommonAncestor(treeNode, p, q))
