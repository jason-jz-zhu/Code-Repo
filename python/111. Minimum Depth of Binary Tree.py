# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# dfs recursion
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        height = min(left_height, right_height) + 1 if left_height > 0 and right_height > 0 else max(left_height, right_height) + 1
        return height

# dfs iterative
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = float('inf')
        while stack:
            curr, height = stack.pop()
            if curr.left:
                stack.append((curr.left, height + 1))
            if curr.right:
                stack.append((curr.right, height + 1))
            if not curr.left and not curr.right:
                res = min(res, height)
        return res

# level traversal
class Solution(object):
    def minDepth(self, root):
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
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                if not node.left and not node.right:
                    return level
            q = tmp
        return level
