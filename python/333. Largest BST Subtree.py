# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if self.isValid(root, float('-inf'), float('inf')):
            return self.count(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def isValid(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.isValid(root.left, minVal, min(maxVal, root.val)) and \
                self.isValid(root.right, max(minVal, root.val), maxVal)

    def count(self, root):
        if not root:
            return 0
        return self.count(root.left) + self.count(root.right) + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SubTree(object):
    def __init__(self, largest, n, min, max):
        self.largest = largest  # largest BST
        self.n = n              # number of nodes in this ST
        self.min = min          # min val in this ST
        self.max = max          # max val in this ST

class Solution(object):
    def largestBSTSubtree(self, root):
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')

        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min, root.val), max(right.max, root.val))
                
