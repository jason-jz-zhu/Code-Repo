"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    subtree, subtreeSum = None, 0
    def findSubtree(self, root):
        # Write your code here
        self.helper(root)
        return self.subtree

    def helper(self, root):
        if root is None:
            return 0
        # dc
        leftSum = self.helper(root.left)
        rightSum = self.helper(root.right)
        # merge
        sum = leftSum + rightSum + root.val
        if self.subtree is None or sum < self.subtreeSum:
            self.subtree = root
            self.subtreeSum = sum
        return sum
