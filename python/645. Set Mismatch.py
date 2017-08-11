# o(n) + o(n)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        hashmap = collections.defaultdict(int)
        dup = missing = -1
        for n in nums:
            hashmap[n] += 1
        for i in xrange(1, len(nums) + 1):
            if i not in hashmap:
                missing = i
            else:
                if hashmap[i] == 2:
                    dup = i
        return [dup, missing]

# o(n) + o(1)
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        dup = missing = -1

        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1

        for i in xrange(len(nums)):
            if nums[i] > 0:
                missing = i + 1
            else:
                nums[i] *= -1
        return [dup, missing]
