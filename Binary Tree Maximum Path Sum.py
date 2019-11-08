"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    打擂台solution
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        self.result = -sys.maxsize
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 0

        leftSum = self.dfs(node.left)
        # if leftSum < 0:
        #     leftSum = 0
        rightSum = self.dfs(node.right)
        # if rightSum < 0:
        #     rightSum = 0

        self.result = max(self.result, node.val + leftSum + rightSum)

        return max(node.val + leftSum, node.val + rightSum, 0)


class MySolution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here

        if not root:
            return 0
        self.result = []
        self.dfs(root)
        return max(self.result)

    def dfs(self, node):
        if not node:
            return 0

        leftSum = self.dfs(node.left)
        if leftSum < 0:
            leftSum = 0
        rightSum = self.dfs(node.right)
        if rightSum < 0:
            rightSum = 0

        nodeSum = max(node.val + leftSum + rightSum, node.val + rightSum, node.val + leftSum, node.val)
        self.result.append(nodeSum)
        return max(node.val + leftSum, node.val + rightSum)
