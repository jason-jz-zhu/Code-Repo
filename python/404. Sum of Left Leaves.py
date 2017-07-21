# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            if cur.left and cur.left.left is None and cur.left.right is None:
                res += cur.left.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
