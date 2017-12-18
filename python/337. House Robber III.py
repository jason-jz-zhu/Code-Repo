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
        return self.helper(root, hashmap)

    def helper(self, root, hashmap):
        if not root:
            return 0
        if root in hashmap:
            return hashmap[root]

        max_val = 0
        if root.left:
            max_val += self.helper(root.left.left, hashmap) + self.helper(root.left.right, hashmap)
        if root.right:
            max_val += self.helper(root.right.left, hashmap) + self.helper(root.right.right, hashmap)

        max_val = max(max_val + root.val, self.helper(root.left, hashmap) + self.helper(root.right, hashmap))
        hashmap[root] = max_val
        return max_val

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
