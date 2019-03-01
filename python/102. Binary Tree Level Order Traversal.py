# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]
        while q:
            res.append([node.val for node in q])
            q = [child for node in q for child in (node.left, node.right) if child]
        return res

# dfs preorder
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        self.helper(node.left, level + 1, res)
        self.helper(node.right, level + 1, res)
