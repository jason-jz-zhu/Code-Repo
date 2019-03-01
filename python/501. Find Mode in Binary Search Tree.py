# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.res = []
        self.cnt = 1
        self.max_cnt = 0
        self.prev = float('-inf')
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)

        if node.val == self.prev:
            self.cnt += 1
        else:
            self.cnt = 1
            self.prev = node.val

        if self.cnt > self.max_cnt:
            self.max_cnt = self.cnt
            self.res = []
            self.res.append(node.val)
        elif self.cnt == self.max_cnt:
            self.res.append(node.val)

        self.dfs(node.right)
