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


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        res = []
        self.helper(root, sum, res)
        return any(res)

    def helper(self, root, target, res):
        if not root.left and not root.right:
            if root.val == target:
                res.append(True)
        if root.left:
            self.helper(root.left, target - root.val, res)
        if root.right:
            self.helper(root.right, target - root.val, res)
