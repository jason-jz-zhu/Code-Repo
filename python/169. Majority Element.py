# using hash
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        for key, value in hash.iteritems():
            if value > len(nums) / 2:
                return key
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
