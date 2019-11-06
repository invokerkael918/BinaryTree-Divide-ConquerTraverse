"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        result = []
        self.dfs(root, target, 0, [], result)
        return result

    def dfs(self, root, target, now_sum, path, result):
        if root is None:
            return
        now_sum += root.val
        path.append(root.val)

        if root.left is None and root.right is None and now_sum == target:
            result.append(path[:])

        self.dfs(root.left, target, now_sum, path, result)
        self.dfs(root.right, target, now_sum, path, result)
        path.pop()
