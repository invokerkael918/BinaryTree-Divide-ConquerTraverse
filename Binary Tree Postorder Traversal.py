"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if not root:
            return
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)
