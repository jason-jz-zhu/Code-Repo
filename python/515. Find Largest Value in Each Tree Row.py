# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [root]
        res = []
        while q:
            res.append(max(node.val for node in q))
            q = [child for node in q for child in (node.left, node.right) if child]
        return res

# dfs preorder
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append(float('-inf'))
        res[level] = max(res[level], node.val)
        self.dfs(node.left, level + 1, res)
        self.dfs(node.right, level + 1, res)
