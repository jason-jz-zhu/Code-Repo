# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTree(low, high):
            res = []
            if low > high:
                res.append(None)
            for i in xrange(low, high + 1):
                left = generateTree(low, i - 1)
                right = generateTree(i + 1, high)
                for j in left:
                    for k in right:
                        cur = TreeNode(i)
                        cur.left = j
                        cur.right = k
                        res.append(cur)
            return res
        if n == 0:
            return []
        return generateTree(1, n)
