class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        stack = []
        for i in reversed(xrange(2 * len(nums))):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            res[i % len(nums)] = stack[-1] if stack else -1
            stack.append(nums[i % len(nums)])
        return ress
