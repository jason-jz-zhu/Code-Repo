# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        import collections
        if not root:
            return False
        q = collections.deque([])
        q.append((root, root.val))
        while q:
            cur, s = q.popleft()
            if not cur.left and not cur.right and s == sum:
                return True
            if cur.left:
                q.append((cur.left, s + cur.left.val))
            if cur.right:
                q.append((cur.right, s + cur.right.val))
        return False


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, sum)

    def dfs(self, root, sum):
        if not root:
            return False
        if not root.right and not root.left:
            return sum == root.val
        left = self.dfs(root.left, sum - root.val)
        right = self.dfs(root.right, sum - root.val)
        return left or right
