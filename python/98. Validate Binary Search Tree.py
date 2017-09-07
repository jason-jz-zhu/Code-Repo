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
        stack = []
        pre = -sys.maxint
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val <= pre:
                    return False
                pre = node.val
                node = node.right
        return True

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

# traverse
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper (root):
            if root:
                helper(root.left)
                if root.val <= self.pre:
                    self.res = False
                    return
                self.pre = root.val
                helper(root.right)

        self.pre = -sys.maxint
        self.res = True
        helper(root)
        return self.res
