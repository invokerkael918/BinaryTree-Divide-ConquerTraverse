# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', A: 'TreeNode', B: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == A or root == B:
            # 找到了A or B return root（A，or B)
            return root
        leftPath = self.lowestCommonAncestor(root.left, A, B)
        # 向左递归
        rightPath = self.lowestCommonAncestor(root.right, A, B)
        # 向右递归
        if leftPath is not None and rightPath is not None:
            # 左右都不为None，此时root为LCA
            return root

        if leftPath is not None:
            # 左边是None从此层return 右边
            return leftPath

        if rightPath is not None:
            # 右边是None从此层return 左边
            return rightPath
        # 都是None return None
        return None
