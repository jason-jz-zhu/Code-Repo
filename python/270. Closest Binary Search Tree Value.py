# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        res = root.val
        while root:
            res = res if abs(res - target) < abs(root.val - target) else root.val
            root = root.left if target < root.val else root.right
        return res

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        k = self.closestValue(kid, target)
        return k if abs(k - target) < abs(root.val - target) else root.val
