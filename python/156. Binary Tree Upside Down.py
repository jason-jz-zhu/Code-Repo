# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.rec(root, None)

    def rec(self, p, parent):
        if not p:
            return parent

        root = self.rec(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None

        p.right = parent
        return root


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        p, parent, parent_right = root, None, None

        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent
