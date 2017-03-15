"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# traverse
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)

# divide conquer
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        # None or leaf
        res = []
        if root is None:
            return res

        # divide/conquer
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        # merge
        res = [root.val] + left + right

        return res

# using stack
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        stack = []
        res = []
        if root is None:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
