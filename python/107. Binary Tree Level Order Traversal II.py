# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, q = [], [root]
        while q:
            res.append([node.val for node in q])
            q = [ kid for node in q for kid in (node.left, node.right) if kid]
        return res[::-1]
