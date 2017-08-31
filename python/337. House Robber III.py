# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        hashmap = {}
        return self.dfs(root, hashmap)

    def dfs(self, root, hashmap):
        if not root:
            return 0
        if root in hashmap:
            return hashmap[root]
        val = 0
        if root.left:
            val += self.dfs(root.left.left, hashmap) + self.dfs(root.left.right, hashmap)
        if root.right:
            val += self.dfs(root.right.left, hashmap) + self.dfs(root.right.right, hashmap)

        val = max(val + root.val, self.dfs(root.left, hashmap) + self.dfs(root.right, hashmap))
        hashmap[root] = val
        return val

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return (0, 0)
            left, right = dfs(root.left), dfs(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))

        return max(dfs(root))
