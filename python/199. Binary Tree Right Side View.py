# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append(q[-1].val)
            q = [ kid for node in q for kid in (node.left, node.right) if kid]
        return res

# dfs node-right-left
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, node, level, res):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        self.helper(node.right, level + 1, res)
        self.helper(node.left, level + 1, res)
