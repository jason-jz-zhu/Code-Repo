# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res, q = [], [root]
        while q:
            res.append(sum([node.val for node in q]) * 1.0 / len(q))
            q = [ kid for node in q for kid in (node.left, node.right) if kid]
        return res
