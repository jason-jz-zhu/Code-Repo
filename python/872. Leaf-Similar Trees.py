# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        tree1_leaves = []
        tree2_leaves = []
        print(tree1_leaves)
        print(tree2_leaves)
        return tree1_leaves == tree2_leaves

    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path.append(node.val)
            return
        self.dfs(node.left, path)
        self.dfs(node.right, path)
