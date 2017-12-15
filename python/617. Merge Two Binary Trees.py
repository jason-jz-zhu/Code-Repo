# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        if t1:
            v1, l1, r1 = t1.val, t1.left, t1.right
        else:
            v1, l1, r1 = 0, None, None
        if t2:
            v2, l2, r2 = t2.val, t2.left, t2.right
        else:
            v2, l2, r2 = 0, None, None
        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(l1, l2)
        node.right = self.mergeTrees(r1, r2)
        return node
