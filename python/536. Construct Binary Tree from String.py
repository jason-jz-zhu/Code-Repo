# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s is None or len(s) == 0:
            return None
        i = s.find('(')
        if i < 0:
            return TreeNode(int(s)) if s else None
        balance = 0
        j = 0
        for idx, val in enumerate(s):
            if val == '(':
                balance += 1
            elif val == ')':
                balance -= 1
            if idx > i and balance == 0:
                j = idx
                break
        root = TreeNode(int(s[: i]))
        root.left = self.str2tree(s[i + 1: j])
        root.right = self.str2tree(s[j + 2: -1])
        return root

# interative
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s is None or len(s) == 0:
            return None
        stack = []
        i = 0
        while i < len(s):
            j = i
            if s[i] == ')':
                stack.pop()
            elif (s[i] >= '0' and s[i] <= '9') or s[i] == '-':
                while i + 1 < len(s) and s[i + 1] >= '0' and s[i + 1] <= '9':
                    i += 1
                curr = TreeNode(int(s[j: i + 1]))
                if stack:
                    top = stack[-1]
                    if not top.left:
                        top.left = curr
                    else:
                        top.right = curr
                stack.append(curr)
            i += 1
        return stack[-1]
