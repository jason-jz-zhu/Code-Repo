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

        return self.helper(root)

    def helper(self, root):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return 1
        min_left = self.helper(root.left)
        min_right = self.helper(root.right)
        return min(min_left, min_right) + 1

# level traversal
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = collections.deque([root])
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.left and not node.right:
                    return res
        return 0
