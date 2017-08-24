# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, start, end):
            if start == end:
                return None
            mid = start + (end - start) / 2
            cur = TreeNode(nums[mid])
            cur.left = helper(nums, start, mid)
            cur.right = helper(nums, mid + 1, end)
            return cur

        return helper(nums, 0, len(nums))
