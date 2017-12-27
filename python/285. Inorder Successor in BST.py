# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# binary serach o(h) o (1)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        res = None
        while root:
            if p.val < root.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res

# dfs interative inorder o(n) o (n)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        flag = False
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if flag:
                    return root
                if root.val == p.val:
                    flag = True
                root = root.right
        return None
