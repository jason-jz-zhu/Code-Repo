# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        q = [(root, 1)]
        while q:
            width = q[-1][-1] - q[0][-1] + 1
            res = max(res, width)
            tmp = []
            for node, i in q:
                if node.left:
                    tmp.append((node.left, i * 2))
                if node.right:
                    tmp.append((node.right, i * 2 + 1))
            q = tmp
        return res

# dfs preorder
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.helper(root, 0, 1, [])
        return self.res

    def helper(self, node, level, idx, left):
        if not node:
            return
        if level == len(left):
            left.append(idx)
        self.res = max(self.res, idx - left[level] + 1)
        self.helper(node.left, level + 1, idx * 2, left)
        self.helper(node.right, level + 1, idx * 2 + 1, left)
