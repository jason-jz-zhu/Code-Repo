# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None
        return self.helper(nums)
    
    def helper(self, nums):
        if not nums:
            return None
        i = nums.index(max(nums))
        node = TreeNode(nums[i])
        node.left = self.helper(nums[: i])
        node.right = self.helper(nums[i + 1:])
        return node