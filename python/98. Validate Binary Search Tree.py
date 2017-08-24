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
