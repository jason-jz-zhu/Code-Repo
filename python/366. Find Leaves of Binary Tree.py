# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def dfs(node, res):
            if not node:
                return -1
            level = 1 + max(dfs(node.left, res), dfs(node.right, res))
            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)
            return level

        res = []
        dfs(root, res)
        return res



class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, cur):
            if not node:
                return None
            if not node.left and not node.right:
                cur.append(node.val)
                return None
            if node.left:
                node.left = dfs(node.left, cur)
            if node.right:
                node.right = dfs(node.right, cur)
            return node
        res = []
        if not root:
            return res
        while root:
            cur = []
            root = dfs(root, cur)
            res.append(cur)
        return res
