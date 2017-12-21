# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = [root.val]
        self.left_helper(root.left, res)
        self.leaves_helper(root, root, res)
        self.right_helper(root.right, res)
        return res

    def left_helper(self, node, res):
        if not node or (not node.left and not node.right):
            return
        res.append(node.val)
        if node.left:
            self.left_helper(node.left, res)
        else:
            self.left_helper(node.right, res)

    def leaves_helper(self, node, root, res):
        if not node:
            return
        self.leaves_helper(node.left, root, res)
        if node != root and not node.left and not node.right:
            res.append(node.val)
        self.leaves_helper(node.right, root, res)

    def right_helper(self, node, res):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            self.right_helper(node.right, res)
        else:
            self.right_helper(node.left, res)
        res.append(node.val)

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        left = [root]
        curr = root.left
        while curr:
          left.append(curr)
          curr = curr.left or curr.right

        right = [root]
        curr = root.right
        while curr:
          right.append(curr)
          curr = curr.right or curr.left

        leaves = []
        stack = [root]
        while stack:
          node = stack.pop()
          if node.right:
            stack.append(node.right)
          if node.left:
            stack.append(node.left)
          if not node.left and not node.right:
            leaves.append(node)

        res = []
        visited = set()
        def visit(node):
          if node not in visited:
            visited.add(node)
            res.append(node.val)

        for node in left: visit(node)
        for node in leaves: visit(node)
        for node in reversed(right): visit(node)

        return res
