# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        foundP = False
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if foundP:
                return root
            if root.val == p.val:
                foundP = True
            root = root.right

        return None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None:
            return None

        found_p = False
        stack = []
        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if found_p:
                    return root
                if root.val == p.val:
                    found_p = True
                root = root.right

        return None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None:
            return None

        successor = None

        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor
