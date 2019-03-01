# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, low, high):
        if low > high:
            return None
        res = []
        for i in range(low, high + 1):
            left = self.dfs(low, i - 1) or [None]
            right = self.dfs(i + 1, high) or [None]
            for l in left:
                for r in right:
                    curr = TreeNode(i)
                    curr.left = l
                    curr.right = r
                    res.append(curr)
        return res
