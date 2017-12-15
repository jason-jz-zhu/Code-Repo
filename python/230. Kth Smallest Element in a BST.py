# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return float('-inf')

        stack = []
        cnt = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                cnt += 1
                if cnt == k:
                    return root.val
                root = root.right
        return float('-inf')

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return float('-inf')

        self.res = 0
        self.cnt = 0
        self.helper(root, k)
        return self.res

    def helper(self, root, k):
        if not root:
            return
        self.helper(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.res = root.val
            return
        self.helper(root.right, k)
