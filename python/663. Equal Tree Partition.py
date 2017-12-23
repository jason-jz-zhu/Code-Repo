# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        hashmap = collections.defaultdict(int)
        root_sum = self.helper(root, hashmap)
        if root_sum == 0:
            return hashmap[root_sum] > 1
        return root_sum % 2 == 0 and (root_sum / 2) in hashmap
    
    def helper(self, node, hashmap):
        if not node:
            return 0
        curr_sum = node.val + self.helper(node.left, hashmap) + self.helper(node.right, hashmap)
        hashmap[curr_sum] += 1
        return curr_sum