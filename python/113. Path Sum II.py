# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, node, sum, path, res):
        if not node:
            return
        if not node.left and not node.right:
            if node.val == sum:
                path.append(node.val)
                res.append(path)
                return
        self.dfs(node.left, sum - node.val, path + [node.val], res)
        self.dfs(node.right, sum - node.val, path + [node.val], res)


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        import collections
        q = collections.deque([])
        q.append((root, root.val, [root.val]))
        while q:
            cur, s, ls = q.popleft()
            if not cur.left and not cur.right and s == sum:
                res.append(ls)
            if cur.left:
                q.append((cur.left, s + cur.left.val, ls + [cur.left.val]))
            if cur.right:
                q.append((cur.right, s + cur.right.val, ls + [cur.right.val]))
        return res
