# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node, s):
            if not node:
                return
            helper(node.right, s)
            node.val += s
            s = node.val
            helper(node.left, s)

        s = 0
        helper(root, s)
        return root

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        s = 0
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node.val += s
                s = node.val
                node = node.left
        return root
