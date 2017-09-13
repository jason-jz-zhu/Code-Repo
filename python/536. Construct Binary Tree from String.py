# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        ix = s.find('(')
        if ix < 0:
            return TreeNode(int(s)) if s else None

        bal = 0
        for jx, u in enumerate(s):
            if u == '(':
                bal += 1
            if u == ')':
                bal -= 1
            if jx > ix and bal == 0:
                break

        root = TreeNode(int(s[: ix]))
        root.left = self.str2tree(s[ix + 1: jx])
        root.right = self.str2tree(s[jx + 2: -1])
        return root
