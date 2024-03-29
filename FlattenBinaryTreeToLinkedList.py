"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):

        if root is None:
            return None

        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)

        # connect

        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        if right_last:
            return right_last
        if left_last:
            return left_last

        return root
