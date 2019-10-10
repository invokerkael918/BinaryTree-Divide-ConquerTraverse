"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    标准答案
    """

    def kthSmallest(self, root, k):
        # use binary tree iterator
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not stack:
                return None

        return stack[-1].val


class Solution1:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        return self.preOrderCreateList(root)[k - 1]

    def preOrderCreateList(self, root):
        if root is None:
            return []
        return self.preOrderCreateList(root.left) + [root.val] + self.preOrderCreateList(root.right)


class Solution2:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # write your code here
        self.result = root.val
        self.count = 0
        self.traverse(root, k)
        return self.result

    def traverse(self, root, k):
        if root == None or self.count >= k:
            return
        self.traverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val

        self.traverse(root.right, k)
