# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return True
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left and right and (not node.left or node.val == node.left.val) and (not node.right or node.val == node.right.val):
            self.res += 1
            return True
        return False
