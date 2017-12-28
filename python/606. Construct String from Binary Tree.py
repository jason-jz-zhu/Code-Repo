# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        s = str(t.val)
        if t.left or t.right:
            s += '(' +self.tree2str(t.left) + ')'
        if t.right:
            s += '(' +self.tree2str(t.right) + ')'
        return s

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        stack = [t]
        visited = set()
        res = ''
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                res += ')'
            else:
                visited.add(node)
                res += '(' + str(node.val)
                if not node.left and node.right:
                    res += '()'
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res[1: -1]
                
