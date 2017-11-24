class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if findNums is None or len(findNums) == 0:
            return []
        if nums is None or len(nums) == 0:
            return []

        stack = []
        hashmap = {}
        for num in nums:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)

        res = []
        for num in findNums:
            res.append(-1 if num not in hashmap else hashmap[num])

        return res
