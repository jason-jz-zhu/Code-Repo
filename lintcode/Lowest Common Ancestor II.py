"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        if root is None:
            return None
        path = set()
        while A is not None:
            path.add(A)
            A = A.parent
        while B not in path:
            B = B.parent
        return B
