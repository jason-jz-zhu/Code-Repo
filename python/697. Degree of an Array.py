class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        if nums is None or len(nums) == 0:
            return 0

        counter = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
        degree = max(counter.values())
        return min(last[v] - first[v] + 1 for v in counter if counter[v] == degree)
