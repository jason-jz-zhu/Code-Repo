class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        import collections
        hashmap = collections.defaultdict(int)

        for i, v in enumerate(nums):
            if v in hashmap and i - hashmap[v] <= k:
                return True
            hashmap[v] = i

        return False

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        hash = {}
        for i in xrange(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = [i]
            else:
                hash[nums[i]].append(i)

        for key, item in hash.iteritems():
            if len(item) > 1:
                for i in xrange(1, len(item)):
                    if abs(item[i] - item[i-1]) <= k:
                        return True

        return False
