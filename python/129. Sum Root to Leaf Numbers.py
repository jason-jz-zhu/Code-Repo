# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.dfs(root, 0)

    def dfs(self, node, s):
        if not node:
            return 0
        if not node.left and not node.right:
            return s * 10 + node.val
        s = s * 10 + node.val
        left = self.dfs(node.left, s)
        right = self.dfs(node.right, s)
        return left + right


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
