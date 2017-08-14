class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        lookup = {}
        for num in nums:
            while stack and num > stack[-1]:
                lookup[stack.pop()] = num
            stack.append(num)
        res = []
        for num in findNums:
            res.append(-1 if num not in lookup else lookup[num])

        return res
