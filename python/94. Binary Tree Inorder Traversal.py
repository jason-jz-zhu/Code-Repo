# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
        res = []
        helper(root, res)
        return res
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def iterative_inorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                list.append(root.val)
                root = root.right
        return list

    def inorderTraversal(self, root):
        list = []
        self.iterative_inorder(root, list)
        return list
