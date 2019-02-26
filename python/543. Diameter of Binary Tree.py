# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
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

        self.res = max(self.res, left + right + 1)
        return max(left, right) + 1


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left) + 1 if node.left else 0
        right = self.dfs(node.right) + 1 if node.right else 0

        self.res = max(self.res, left + right)
        return max(left, right)
