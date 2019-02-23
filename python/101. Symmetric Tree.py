# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        outer = self.dfs(left.left, right.right)
        inner = self.dfs(left.right, right.left)
        return outer and inner and left.val == right.val

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        queue = [root]
        while queue:
            tmp = [kid for node in queue if node for kid in (node.left, node.right)]
            if self.helper(tmp):
                queue = tmp
            else:
                return False
        return True

    def helper(self, nodes):
        cache = [node.val if node else '#' for node in nodes]
        return cache == cache[::-1]

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)

        return True
