"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        res = []
        if root is None:
            return res
        path = []
        sum = 0
        self.helper(root, target, path, sum, res)
        return res
    def helper(self, root, target, path, sum, res):
        if root is None:
            return

        path.append(root.val)
        sum += root.val

        if root.left is None and root.right is None and sum == target:
            res.append(path[:])

        self.helper(root.left, target, path, sum, res)
        self.helper(root.right, target, path, sum, res)

        path.pop()
        sum -= root.val
