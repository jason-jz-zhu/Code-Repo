class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        hashmap = {}

        for i in xrange(len(nums)):
            tmp = target - nums[i]
            if tmp in hashmap:
                return [hashmap[tmp], i]
            hashmap[nums[i]] = i

        return []


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

        return []
