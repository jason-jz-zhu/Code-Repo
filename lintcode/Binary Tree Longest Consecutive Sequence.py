# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    longest = 0
    def longestConsecutive(self, root):
        # Write your code here
        self.helper(root)
        return self.longest

    def helper(self, root):
        if not root:
            return 0

        left_len = self.helper(root.left)
        right_len = self.helper(root.right)

        cur_len = 1

        if root.left and root.left.val == root.val + 1:
            cur_len = max(cur_len, left_len + 1)
        if root.right and root.right.val == root.val + 1:
            cur_len = max(cur_len, right_len + 1)

        self.longest = max(self.longest, cur_len, left_len, right_len)

        return cur_len
