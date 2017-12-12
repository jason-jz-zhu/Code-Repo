# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        cache = collections.defaultdict(int)
        cache[0] = 1
        self.res = 0
        self.helper(root, sum, 0, cache)
        return self.res

    def helper(self, root, target, curSum, cache):
        if not root:
            return
        tmp = curSum + root.val - target
        if tmp in cache:
            self.res += cache[tmp]
        cache[curSum + root.val] += 1
        self.helper(root.left, target, curSum + root.val, cache)
        self.helper(root.right, target, curSum + root.val, cache)
        cache[curSum + root.val] -= 1


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfs(root, val):
            if not root:
                return 0
            res = (val == root.val)
            res += dfs(root.left, val - root.val)
            res += dfs(root.right, val - root.val)
            return res

        if not root:
            return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
