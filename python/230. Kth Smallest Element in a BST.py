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

        Solution.res = 0
        Solution.cnt = 0
        self.helper(root, k)
        return Solution.res

    def helper(self, root, k):
        if root:
            self.helper(root.left, k)
            Solution.cnt += 1
            if Solution.cnt == k:
                Solution.res = root.val
                return
            self.helper(root.right, k)
