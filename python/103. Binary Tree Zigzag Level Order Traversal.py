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

        q = [root]
        level = 0
        res = []

        while q:
            level += 1
            tmp = [node.val for node in q]
            if level % 2:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            q = [kid for node in q for kid in (node.left, node.right) if kid]

        return res
