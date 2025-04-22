# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.depth = 0
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        
        self.depth += 1
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        
        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_max = self.maxDepth(root.left)
        r_max = self.maxDepth(root.right)
        res = max(l_max, r_max) + 1
        return res

# --------------------



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
