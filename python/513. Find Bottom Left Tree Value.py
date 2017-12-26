# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None

        res, q = 0, [root]
        while q:
            res= q[0].val
            q = [ kid for node in q for kid in (node.left, node.right) if kid]
        return res

# dfs preorder
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level = 0
        res = [0, 0]
        self.helper(root, level, res)
        return res[0]

    def helper(self, node, level, res):
        if not node:
            return
        if level == res[1]:
            res[0] = node.val
            res[1] += 1
        self.helper(node.left, level + 1, res)
        self.helper(node.right, level + 1, res)
