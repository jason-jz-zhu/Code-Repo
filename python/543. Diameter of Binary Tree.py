# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiagmeter = 0
        self.maxDepth(root)
        return self.maxDiagmeter

    def maxDepth(self, root):
        if root is None:
            return 0

        l_max = self.maxDepth(root.left)
        r_max = self.maxDepth(root.right)

        cur_diameter = l_max + r_max
        self.maxDiagmeter = max(self.maxDiagmeter, cur_diameter)
        return 1 + max(l_max, r_max)



#----------------2025--------- 

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res - 1

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.res = max(self.res, left + right + 1)
        return max(left, right) + 1


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left) + 1 if node.left else 0
        right = self.dfs(node.right) + 1 if node.right else 0

        self.res = max(self.res, left + right)
        return max(left, right)
