# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.res = []
        self.prev = float('-inf')
        self.cnt = 1
        self.max_cnt = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return

        self.helper(root.left)

        if root.val != self.prev:
            self.cnt = 1
            self.prev = root.val
        else:
            self.cnt += 1

        if self.cnt > self.max_cnt:
            self.max_cnt = self.cnt
            self.res = []
            self.res.append(root.val)
        elif self.cnt == self.max_cnt:
            self.res.append(root.val)

        self.helper(root.right)
