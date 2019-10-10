"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:

    def findSubtree(self, root):
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum

        return sum, root, sum


class Solution2:
    def findSubtree(self, root):
        self.minumum_weight = sys.maxsize
        self.subtree = None
        self.helper(root)

        return self.subtree

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.minumum_weight:
            self.minumum_weight = root_weight
            self.subtree = root

        return root_weight