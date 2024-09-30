
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfTree(treeNode):
    # Initialize a global variable to store the maximum diameter
    global diameteris
    diameteris = 0

    # Define a helper function to calculate the depth of the tree
    def depth(node):
        global diameteris  # Declare the global variable inside the function

        # If the node is None, return 0 (base case)
        if node is None:
            return 0


        # Recursively calculate the depth of the left and right subtrees
        left = depth(node.left)
        right = depth(node.right)

        # Update the maximum diameter found so far
        diameteris = max(diameteris, left + right )

        # Return the depth of the current node
        return max(left, right) + 1

    # Call the helper function with the root of the tree
    depth(treeNode)

    # Return the maximum diameter found
    return diameteris


treeNode = TreeNode(3)
treeNode.left = TreeNode(9)
treeNode.right = TreeNode(20)
treeNode.right.left = TreeNode(15)
treeNode.right.right = TreeNode(7)

print(diameterOfTree(treeNode))
