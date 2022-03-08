# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# dfs preorder
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 1
        self.dfs(root, 1)
        return self.res
    
    def dfs(self, root, depth):
        if not root:
            return 0
        if not root.left and not root.right:
            self.res = max(self.res, depth)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)


# dfs postorder
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.maxDepth(root.right) + 1
        if not root.right:
            return self.maxDepth(root.left) + 1
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1


# dfs recursion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# dfs iterative
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            curr, level = stack.pop()
            res = max(res, level)
            if curr.left:
                stack.append((curr.left, level + 1))
            if curr.right:
                stack.append((curr.right, level + 1))
        return res


# level traversal
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level = 0
        q = [root]
        while q:
            level += 1
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return level
