"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here

        AParent = set()
        while A is not root:
            AParent.add(A)
            A = A.parent

        while B is not root:
            if B in AParent:
                return B
            B = B.parent

        return root

class MySolution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here

        levelA = self.getLevel(root, A)
        levelB = self.getLevel(root, B)
        if levelA < levelB:
            dif = levelB - levelA
            for i in range(dif):
                B = B.parent
        if levelB < levelA:
            dif = levelA - levelB
            for i in range(dif):
                A = A.parent

        if A is B:
            return A

        while A is not B:
            A = A.parent
            B = B.parent
        return B

    def getLevel(self, root, node):
        if node is root:
            return 0
        level = 0
        while node is not root:
            level += 1
            node = node.parent
        return level




