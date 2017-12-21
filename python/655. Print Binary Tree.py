# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []

        self.rows = self.get_height(root)
        self.cols = 2 ** self.rows - 1
        self.res = [['' for _ in range(self.cols)] for _ in range(self.rows)]

        self.helper(root, 0, 0)
        return self.res

    def helper(self, node, level, pos):
        if not node:
            return
        left_padding = 2 ** (self.rows - level - 1) - 1
        spacing = 2 ** (self.rows - level) - 1
        index = left_padding + pos * (spacing + 1)
        self.res[level][index] = str(node.val)
        self.helper(node.left, level + 1, pos << 1)
        self.helper(node.right, level + 1, (pos << 1) + 1)

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
            
