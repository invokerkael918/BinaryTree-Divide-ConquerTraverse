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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = []
        result = []
        node = root
        while node:
            stack.append(node)
            node = node.left

        while stack:
            currNode = stack.pop()
            result.append(currNode.val)

            if currNode.right:
                currNode = currNode.right
                while currNode:
                    stack.append(currNode)
                    currNode = currNode.left
        return result


class Solution2:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if not root:
            return
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
