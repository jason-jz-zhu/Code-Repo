# boyer-moore vote algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, cnt = None, 0

        for num in nums:
            if num == majority:
                cnt += 1
            elif cnt == 0:
                cnt, majority = 1, num
            else:
                cnt -= 1
        return majority

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
