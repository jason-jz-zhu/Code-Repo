# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        prev_sum = collections.defaultdict(int)
        prev_sum[0] = 1
        self.res = 0
        self.dfs(root, sum, 0, prev_sum)
        return self.res

    def dfs(self, node, sum, curr_sum, prev_sum):
        if not node:
            return
        curr_sum = curr_sum + node.val
        old_sum = curr_sum - sum
        if old_sum in prev_sum:
            self.res += prev_sum[old_sum]
        prev_sum[curr_sum] += 1
        self.dfs(node.left, sum, curr_sum, prev_sum)
        self.dfs(node.right, sum, curr_sum, prev_sum)
        prev_sum[curr_sum] -= 1


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        self.res = 0
        self.dfs(root, sum)
        return self.res

    def dfs(self, node, sum):
        if not node:
            return
        self.validate_path(node, sum)
        self.dfs(node.left, sum)
        self.dfs(node.right, sum)

    def validate_path(self, node, target):
        if not node:
            return
        if node.val == target:
            self.res += 1
        self.validate_path(node.left, target - node.val)
        self.validate_path(node.right, target - node.val)
