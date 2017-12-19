# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return -1
        level = 1 + max(self.helper(root.left, res), self.helper(root.right, res))
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        return level



class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        while root:
            curr = []
            root = self.helper(root, curr)
            res.append(curr)
        return res

    def helper(self, root, curr):
        if not root:
            return None
        if not root.left and not root.right:
            curr.append(root.val)
            return None
        if root.left:
            root.left = self.helper(root.left, curr)
        if root.right:
            root.right = self.helper(root.right, curr)
        return root
