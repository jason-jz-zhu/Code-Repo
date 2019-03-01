# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        freq = collections.defaultdict(int)
        self.dfs(root, freq)
        max_freq = max(freq.values())
        return [s for s, freq in freq.items() if freq == max_freq]

    def dfs(self, node, freq):
        if not node:
            return 0
        left = self.dfs(node.left, freq)
        right = self.dfs(node.right, freq)
        s = left + right + node.val
        freq[s] += 1
        return s
