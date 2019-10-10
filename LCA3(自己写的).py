"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)

        if a and b:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_lca = self.helper(root.left, A, B)
        right_a, right_b, right_lca = self.helper(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        if root == A or root == B:
            return a, b, root

        if left_lca and right_lca:
            return a, b, root

        if left_lca:
            return a, b, left_lca

        if right_lca:
            return a, b, right_lca

        return a, b, None
