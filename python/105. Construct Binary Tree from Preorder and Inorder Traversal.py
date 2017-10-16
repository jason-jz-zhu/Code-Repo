# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder is None or len(preorder) == 0:
            return None
        if inorder is None or len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_pos + 1], inorder[: root_pos])
        root.right = self.buildTree(preorder[root_pos + 1:], inorder[root_pos + 1:])
        return root
