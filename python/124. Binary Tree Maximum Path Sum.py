# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0

        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        self.res = max(self.res, node.val + left + right)
        return max(left, right) + node.val


# Find the maximum path sum between two leaves of a binary tree
# https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
def solution(root):
    if not root:
        return 0

    res = [float('-inf')]
    dfs(root, res)
    return res[0]

def dfs(node, res):
    if not node:
        return 0

    left = dfs(node.left, res)
    right = dfs(node.right, res)

    if node.left and node.right:
        res[0] = max(res[0], left + right + node.val)
    return max(left, right) + node.val
