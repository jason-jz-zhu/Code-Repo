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
        isBBT, _ = self.helper(root)
        return isBBT
    def helper(self, root):
        if root is None:
            return True, 0
        left_isBBT, left_height = self.helper(root.left)
        right_isBBT, right_height = self.helper(root.right)
        if not left_isBBT or not right_isBBT:
            return False, 0
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
