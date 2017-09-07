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
        self.cnt = 0
        self.helper(root)
        return self.cnt

    def helper(self, root):
        if not root:
            return True

        l, r = self.helper(root.left), self.helper(root.right)
        if l and r and (not root.left or root.left.val == root.val) and \
        (not root.right or root.right.val == root.val):
            self.cnt += 1
            return True
        return False
