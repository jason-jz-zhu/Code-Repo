"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
# traverse plus divide conquer
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    # global variables
    subtree, subtreeResult = None, 0
    def findSubtree2(self, root):
        # Write your code here
        self.helper(root)
        return self.subtree

    def helper(self, root):
        # node is None or leaf
        if root is None:
            return 0, 0
        # divide / conquer
        leftSum, leftSize = self.helper(root.left)
        rightSum, rightSize = self.helper(root.right)
        # merge
        sum = leftSum + rightSum + root.val
        size = leftSize + rightSize + 1
        if self.subtree is None or sum * 1.0 / size > self.subtreeResult:
            self.subtree = root
            self.subtreeResult = sum * 1.0 / size
        return sum, size
