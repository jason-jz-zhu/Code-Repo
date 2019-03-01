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
        cache = collections.defaultdict(int)
        return self.dfs(root, cache)

    def dfs(self, node, cache):
        if not node:
            return 0
        if node in cache:
            return cache[node]
        s = 0
        if node.left:
            s += self.dfs(node.left.left, cache) + self.dfs(node.left.right, cache)
        if node.right:
            s += self.dfs(node.right.left, cache) + self.dfs(node.right.right, cache)
        s = max(node.val + s, self.dfs(node.left, cache) + self.dfs(node.right, cache))
        cache[node] = s
        return s

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
