# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or len(inorder) == 0:
            return None
        if postorder is None or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: root_pos], postorder[: root_pos])
        root.right = self.buildTree(inorder[root_pos + 1:], postorder[root_pos: -1])
        return root

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or len(inorder) == 0:
            return None
        if postorder is None or len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        i, j = len(postorder) - 2, len(inorder) - 1
        while i >= 0:
            curr = stack[-1]
            if curr.val != inorder[j]:
                right = TreeNode(postorder[i])
                curr.right = right
                stack.append(right)
                i -= 1
            else:
                while stack and stack[-1].val == inorder[j]:
                    curr = stack.pop()
                    j -= 1
                left = TreeNode(postorder[i])
                curr.left = left
                stack.append(left)
                i -= 1
        return root
