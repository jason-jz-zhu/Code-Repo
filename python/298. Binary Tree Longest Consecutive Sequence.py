# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        self.helper(root, float('inf'), 0)
        return self.res

    def helper(self, root, pre_val, curr_cnt):
        if not root:
            return
        if root.val == pre_val + 1:
            curr_cnt += 1
        else:
            curr_cnt = 1
        self.res = max(self.res, curr_cnt)
        self.helper(root.left, root.val, curr_cnt)
        self.helper(root.right, root.val, curr_cnt)
