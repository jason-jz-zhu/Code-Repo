class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        counter = collections.Counter(nums)
        return sum([1 for val in counter.values() if val > 1]) > 0


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        hashmap = collections.defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        for val in hashmap.values():
            if val > 1:
                return True

        return False
