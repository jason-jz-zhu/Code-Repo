# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs(root))

    def dfs(self, node):
        if not node:
            return [0, 0]
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        not_include_node_max = max(left) + max(right)
        include_node_max = node.val + left[0] + right[0]
        return [not_include_node_max, include_node_max]

    
