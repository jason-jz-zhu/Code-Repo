# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        level = 0
        q = [root]
        while q:
            if level % 2:
                res.append([node.val for node in q[::-1]])
            else:
                res.append([node.val for node in q])
            level += 1
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res

# dfs preorder
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, node, level, res):
        if not node:
            return
        if len(res) == level:
            res.append([])
        if level % 2:
            res[level].insert(0, node.val)
        else:
            res[level].append(node.val)
        self.helper(node.left, level + 1, res)
        self.helper(node.right, level + 1, res)
