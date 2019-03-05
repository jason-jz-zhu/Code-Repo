# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs interative
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

# dfs recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if not node:
            return
        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)

# Morris Traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        curr = root
        prev = None
        while curr:
            if not curr.left:
                res.append(curr.val)
                prev = curr
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if not node.right:
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    res.append(curr.val)
                    prev = curr
                    curr = curr.right
        return res
