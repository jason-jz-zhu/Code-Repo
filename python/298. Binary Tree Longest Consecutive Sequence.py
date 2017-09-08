# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = [0]
        self.dfs(root, float('inf'), 0, res)
        return res[0]

    def dfs(self, root, preVal, curCnt, res):
        if not root:
            return
        if root.val == preVal + 1:
            curCnt += 1
        else:
            curCnt = 1
        res[0] = max(res[0], curCnt)
        self.dfs(root.left, root.val, curCnt, res)
        self.dfs(root.right, root.val, curCnt, res)
