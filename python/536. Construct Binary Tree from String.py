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
        i = s.find('(')
        if i < 0:
            return TreeNode(int(s)) if s else None

        balance = 0
        for j, c in enumerate(s):
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
            if j > i and balance == 0:
                break

        root = TreeNode(int(s[: i]))
        root.left = self.str2tree(s[i + 1: j])
        root.right = self.str2tree(s[j + 2: -1])
        return root
