# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left_max = left + 1 if node.left and node.val == node.left.val else 0
        right_max = right + 1 if node.right and node.val == node.right.val else 0
        self.res = max(self.res, left_max + right_max)

        return max(left_max, right_max)


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = 0
        self.dfs(root)
        return self.res - 1

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left_max = left + 1 if node.left and node.val == node.left.val else 1
        right_max = right + 1 if node.right and node.val == node.right.val else 1
        if node.left and node.right:
            self.res = max(self.res, left_max + right_max - 1)
        elif node.left:
            self.res = max(self.res, left_max)
        elif node.right:
            self.res = max(self.res, right_max)
        else:
            self.res = max(self.res, 1)
        return max(left_max, right_max)
