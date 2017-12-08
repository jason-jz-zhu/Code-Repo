# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        is_bbt, height = self.helper(root)
        return is_bbt

    def helper(self, root):
        if not root:
            return True, 0
        left_is_bbt, left_height = self.helper(root.left)
        right_is_bbt, right_height = self.helper(root.right)
        if not left_is_bbt or not right_is_bbt:
            return False, 0
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
