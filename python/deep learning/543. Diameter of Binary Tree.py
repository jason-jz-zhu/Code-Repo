# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.res = 0
        self.dfs(root)
        return Solution.res

    def dfs(self, root):
        if not root:
            return 0

        left, right = self.dfs(root.left), self.dfs(root.right)
        Solution.res = max(Solution.res, left + right)

        return max(left, right) + 1
