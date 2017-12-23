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
        self.helper(root, root)
        return self.res
    
    def helper(self, node, parent):
        if not node:
            return 0, 0
        li, ld =self.helper(node.left, node)
        ri, rd = self.helper(node.right, node)
        self.res = max(self.res, li + rd + 1, ld + ri + 1)
        if node.val == parent.val + 1:
            return max(li, ri) + 1, 0
        if node.val == parent.val - 1:
            return 0, max(ld, rd) + 1
        return 0, 0