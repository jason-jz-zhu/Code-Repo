# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, num):
        if not root:
            return
        if not root.left and not root.right:
            self.res += num * 10 + root.val
        if root.left:
            self.dfs(root.left, num * 10 + root.val)
        if root.right:
            self.dfs(root.right, num * 10 + root.val)


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

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q, res = collections.deque([(root, root.val)]), 0
        while q:
            node, value = q.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    q.append((node.left, value*10+node.left.val))
                if node.right:
                    q.append((node.right, value*10+node.right.val))
        return res
