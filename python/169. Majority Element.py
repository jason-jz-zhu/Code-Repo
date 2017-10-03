# using hash
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        if nums is None or len(nums) == 0:
            return None
        counter = collections.Counter(nums)
        for num, cnt in counter.iteritems():
            if cnt > len(nums)/2:
                return num
        return None

# boyer-moore vote algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, count = nums[0], 1
        for i in xrange(1, len(nums)):
            if count == 0:
                count += 1
                majority = nums[i]
                continue
            elif nums[i] == majority:
                count += 1
            else:
                count -= 1
        return majority
