# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
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
            return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left and right and (not root.left or root.left.val == root.val) and \
        (not root.right or root.right.val == root.val):
            self.res += 1
            return True
        return False
