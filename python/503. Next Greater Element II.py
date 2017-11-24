class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        stack = []
        res = [0] * len(nums)
        size = len(nums)
        for i in reversed(range(2 * size)):
            while stack and stack[-1] <= nums[i % size]:
                stack.pop()
            res[i % size] = stack[-1] if stack else -1
            stack.append(nums[i % size])

        return res

        
