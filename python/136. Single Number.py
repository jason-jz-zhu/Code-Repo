class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for key, val in hashmap.items():
            if val == 1:
                return key
            
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)
