# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        new_sum = sum - root.val
        left = self.hasPathSum(root.left, new_sum)
        right = self.hasPathSum(root.right, new_sum)
        return left or right

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
