# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        p_left = left + 1 if root.left and root.val == root.left.val else 0
        p_right = right + 1 if root.right and root.val == root.right.val else 0
        self.res = max(self.res, p_left + p_right)
        return max(p_left, p_right)
