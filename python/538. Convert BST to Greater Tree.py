# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.s = 0
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.right)
        node.val += self.s
        self.s = node.val
        self.dfs(node.left)

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
