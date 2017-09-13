# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [(root, 1)]
        res = 0
        while q:
            width = q[-1][-1] - q[0][-1] + 1
            res = max(res, width)
            tmp = []
            for n, i in q:
                if n.left:
                    tmp.append((n.left, i * 2))
                if n.right:
                    tmp.append((n.right, i * 2 + 1))
            q = tmp
        return res
