# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import collections
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        hashmap = collections.defaultdict(int)
        res = []
        self.helper(root, hashmap, res)
        return res

    def helper(self, root, hashmap, res):
        if root:
            tuple = root.val, self.helper(root.left, hashmap, res), \
                self.helper(root.right, hashmap, res)
            if hashmap[tuple] == 1:
                res.append(root)
            hashmap[tuple] += 1
            return tuple
