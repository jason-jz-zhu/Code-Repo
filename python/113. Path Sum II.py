# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)


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
