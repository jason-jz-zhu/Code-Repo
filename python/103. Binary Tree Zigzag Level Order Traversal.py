# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res, stack, level = [], [root], 1
        while stack:
            tmp = [node.val for node in stack]
            if level % 2:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]
            level += 1
        return res
