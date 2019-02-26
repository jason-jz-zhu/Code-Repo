# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return -1
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)
        level = max(left, right) + 1
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level
