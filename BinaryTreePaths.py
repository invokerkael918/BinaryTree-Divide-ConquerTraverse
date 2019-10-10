"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution3:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    Input:
       1
     /  \
    2    3
     \
      5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
    """

    def binaryTreePaths(self, root):
        queue = deque(root)








class Solution1:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()

        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()


class Solution2:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)

        paths = []
        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)

        return paths




