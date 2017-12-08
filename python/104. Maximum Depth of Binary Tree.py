# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0
        max_left = self.helper(root.left)
        max_right = self.helper(root.right)
        return max(max_left, max_right) + 1

# level traversal
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        q = collections.deque([root])

        while q:
            res += 1
            q = [kid for node in q for kid in (node.left, node.right) if kid]

        return res
