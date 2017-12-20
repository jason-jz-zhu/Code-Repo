# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.helper(root.right)
        curr = root
        if not curr.left:
            return
        curr = curr.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
        root.right = root.left
        root.left = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            if stack:
                node.right = stack[-1]
            else:
                node.right = None
