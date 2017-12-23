# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        q = [root]
        while q:
            d -= 1
            if d == 0:
                return root
            if d == 1:
                for node in q:
                    node.left, node.left.left = TreeNode(v), node.left
                    node.right, node.right.right = TreeNode(v), node.right
            else:
                q = [kid for node in q for kid in (node.left, node.right) if kid]
        return root

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None
        dummy, dummy.left = TreeNode(None), root
        q = [dummy]
        for _ in range(d - 1):
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        for node in q:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        self.helper(root, v, d, 1)
        return root
    
    def helper(self, node, v, d, curr):
        if not node:
            return 
        if curr == d - 1:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
            return 
        self.helper(node.left, v, d, curr + 1)
        self.helper(node.right, v, d, curr + 1)