# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        t1 = self.preorder(s, True)
        t2 = self.preorder(t, True)
        if t2 in t1:
            return True
        return False

    def preorder(self, t, left):
        if not t:
            if left:
                return 'lnull'
            else:
                return 'rnull'

        return '#' + str(t.val) + self.preorder(t.left, True) + self.preorder(t.right, False)



class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and \
                   isSame(x.left, y.left) and \
                   isSame(x.right, y.right)

        def preOrderTraverse(s, t):
            return s != None and \
                   (isSame(s, t) or \
                    preOrderTraverse(s.left, t) or \
                    preOrderTraverse(s.right, t))

        return preOrderTraverse(s, t)
