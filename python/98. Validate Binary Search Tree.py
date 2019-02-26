# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, min_v, max_v):
        if not node:
            return True

        if node.val <= min_v or node.val >= max_v:
            return False

        left = self.dfs(node.left, min_v, node.val)
        right = self.dfs(node.right, node.val, max_v)

        return left and right

# traverse
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.res = True
        self.prev = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if root:
            self.helper(root.left)
            if root.val <= self.prev:
                self.res = False
                return
            self.prev = root.val
            self.helper(root.right)

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = []
        prev = float('-inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= prev:
                    return False
                prev = root.val
                root = root.right
        return True
