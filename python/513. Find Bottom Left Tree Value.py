# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
