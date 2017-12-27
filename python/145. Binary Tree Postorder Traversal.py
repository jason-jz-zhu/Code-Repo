# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs interative 1
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [(root, 'visit')]
        res = []
        while stack:
            node, flag = stack.pop()
            if flag == 'visit':
                stack.append((node, 'get'))
                if node.right:
                    stack.append((node.right, 'visit'))
                if node.left:
                    stack.append((node.left, 'visit'))
            else:
                res.append(node.val)
        return res

# dfs interative 2
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]

# dfs recursive
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if not node:
            return
        self.helper(node.left, res)
        self.helper(node.right, res)
        res.append(node.val)
