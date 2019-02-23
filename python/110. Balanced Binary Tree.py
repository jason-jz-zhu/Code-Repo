# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        h, res = self.dfs(root)
        return res

    def dfs(self, node):
        if not node:
            return 0, True
        left_height, left_validate = self.dfs(node.left)
        right_height, right_validate = self.dfs(node.right)
        validate = True if left_validate and right_validate and abs(left_height - right_height) <= 1 else False
        height = max(left_height, right_height) + 1
        return height, validate
