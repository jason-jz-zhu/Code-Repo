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


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or len(inorder) == 0:
            return None
        if preorder is None or len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        i, j = 1, 0
        while i < len(preorder):
            curr = stack[-1]
            if curr.val != inorder[j]:
                #as long as we have not reach the leftmost node we can safely follow left path and attach left child
                left = TreeNode(preorder[i])
                curr.left = left
                stack.append(left)
                i += 1
            else:
                #found the node from stack where we have not visited its right subtree
                while stack and stack[-1].val == inorder[j]:
                    curr = stack.pop()
                    j += 1
                right = TreeNode(preorder[i])
                curr.right = right
                stack.append(right)
                i += 1
        return root
