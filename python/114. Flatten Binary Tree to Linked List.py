# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dc
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if root is None:
            return None
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        if right:
            return right

        if left:
            return left

        return root

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        s = []
        s.append(root)
        while s:
            node = s.pop()
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
            node.left = None
            if s:
                node.right = s[-1]
            else:
                node.right = None
