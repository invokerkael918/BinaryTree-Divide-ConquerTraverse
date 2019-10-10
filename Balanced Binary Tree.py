"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

class MySolution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if abs(leftHeight - rightHeight)>1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, node):
        if node is None:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)

        return max(left,right)+1


