# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        vals = []
        self.inorder(root, vals)
        res = TreeNode(0)
        curr = res
        for val in vals:
            curr.right = TreeNode(val)
            curr = curr.right
        return res.right

    def inorder(self, root, vals):
        if not root:
            return
        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        res = self.curr = TreeNode(0)
        self.inorder(root)
        return res.right

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        root.left = None
        self.curr.right = root
        self.curr = root
        self.inorder(root.right)
        
