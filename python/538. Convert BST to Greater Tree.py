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
        if not root:
            return None
        self.s = 0
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        self.helper(root.right)
        root.val += self.s
        self.s = root.val
        self.helper(root.left)

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
