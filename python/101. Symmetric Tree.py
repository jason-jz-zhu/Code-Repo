# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False

        outer = self.helper(left.left, right.right)
        inner = self.helper(left.right, right.left)
        return outer and inner

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isSymmetricRecu(root.left, root.right)

    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
