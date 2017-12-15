# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.m_first = root.val
        self.m_second = float('inf')
        self.helper(root)
        return -1 if self.m_second == float('inf') else self.m_second

    def helper(self, root):
        if not root:
            return
        if self.m_first < root.val < self.m_second:
            self.m_second = root.val
        self.helper(root.left)
        self.helper(root.right)
