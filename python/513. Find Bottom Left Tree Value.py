# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [root]
        res = 0
        while q:
            res = q[0].val
            q = [child for node in q for child in (node.left, node.right) if child]
        return res

# dfs preorder
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = {
            'left_node_val': 0,
            'curr_level': 0
        }
        self.dfs(root, 0, res)
        return res['left_node_val']

    def dfs(self, node, level, res):
        if not node:
            return
        if level == res['curr_level']:
            res['curr_level'] += 1
            res['left_node_val'] = node.val
        self.dfs(node.left, level + 1, res)
        self.dfs(node.right, level + 1, res)
