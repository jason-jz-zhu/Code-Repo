# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []

        count = collections.Counter()
        res = []
        self.dfs(root, count, res)
        return res

    def dfs(self, node, count, res):
        if not node:
            return '#'
        left = self.dfs(node.left, count, res)
        right = self.dfs(node.right, count, res)
        path = '{},{},{}'.format(left, right, node.val)
        count[path] += 1
        if count[path] == 2:
            res.append(node)
        return path
