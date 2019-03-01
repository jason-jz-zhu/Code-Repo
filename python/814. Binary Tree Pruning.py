# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return False
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None
        return node.val == 1 or left or right

    
