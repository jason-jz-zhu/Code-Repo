# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append(sum([node.val for node in q]) / len(q))
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res

# dfs preorder
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        cache = []
        res = []
        self.helper(root, 0, cache)
        for values in cache:
            res.append((sum(values) * 1.0) / len(values))
        return res

    def helper(self, node, level, cache):
        if not node:
            return
        if level == len(cache):
            cache.append([])
        cache[level].append(node.val)
        self.helper(node.left, level + 1, cache)
        self.helper(node.right, level + 1, cache)
