
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = []
        prev = float('-inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= prev:
                    return False
                prev = root.val
                root = root.right
        return True

# traverse
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.res = True
        self.prev = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root):
        if root:
            self.helper(root.left)
            if root.val <= self.prev:
                self.res = False
                return
            self.prev = root.val
            self.helper(root.right)

# Divide and Conquer
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, minVal, maxVal):
        if not root:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        return self.helper(root.left, minVal, min(maxVal, root.val)) and \
                self.helper(root.right, max(minVal, root.val), maxVal)
