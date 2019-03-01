# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return None

        h = self.get_height(root)
        w = 2 ** h - 1
        res = [['' for _ in range(w)] for _ in range(h)]
        self.dfs(root, 0, 0, w - 1, res)
        return res

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def dfs(self, node, level, left, right, res):
        if not node:
            return
        mid = (left + right) // 2
        res[level][mid] = str(node.val)
        self.dfs(node.left, level + 1, left, mid - 1, res)
        self.dfs(node.right, level + 1, mid + 1, right, res)
