"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# divide conquer
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# traverse
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    depth = 0

    def maxDepth(self, root):
        # write your code here
        self.helper(root, 1)
        return self.depth

    def helper(self, root, cDepth):
        if root is None:
            return
        if cDepth > self.depth:
            self.depth = cDepth
        self.helper(root.left, cDepth + 1)
        self.helper(root.right, cDepth + 1)
