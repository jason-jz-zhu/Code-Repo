# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, s):
        if not root:
            return
        if not root.left and not root.right:
            self.res += s
        if root.left:
            self.dfs(root.left, s * 10 + root.left.val)
        if root.right:
            self.dfs(root.right, s * 10 + root.right.val)


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        q = collections.deque([(root, root.val)])
        while q:
            node, num = q.popleft()
            if not node.left and not node.right:
                res += num
            if node.left:
                q.append((node.left, num * 10 + node.left.val))
            if node.right:
                q.append((node.right, num * 10 + node.right.val))
        return res



class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, sum):
        if not root:
            return 0

        if not root.left and not root.right:
            return sum * 10 + root.val

        return self.dfs(root.left, sum * 10 + root.val) + self.dfs(root.right, sum * 10 + root.val)
