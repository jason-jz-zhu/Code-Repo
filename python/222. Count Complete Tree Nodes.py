# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        hLeft = self.leftHeight(root)
        hRight = self.rightHeight(root)
        if hLeft == hRight:
            return 2 ** hLeft - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def leftHeight(self, root):
        return self.leftHeight(root.left) + 1 if root else 0

    def rightHeight(self, root):
        return self.rightHeight(root.right) + 1 if root else 0
