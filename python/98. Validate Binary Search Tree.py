# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = None
        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if p.val <= pre:
                return False
            pre = p.val
            p = p.right

        return True

# traverse
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    pre = None
    isBST = True
    def isValidBST(self, root):
        # write your code here
        self.traverse(root)
        return self.isBST

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.pre is not None and self.pre >= root.val:
            self.isBST = False
            return
        self.pre = root.val
        self.traverse(root.right)
