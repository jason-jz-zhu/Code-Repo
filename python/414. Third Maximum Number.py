class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(set(nums)) < 3:
            return max(nums)

        first = second = third = -sys.maxint - 1
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif second < num < first:
                second, third = num, second
            elif third < num < second:
                third = num
        return third

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(set(nums)) < 3:
            return max(nums)

        heap = []
        for num in set(nums):
            heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        return heapq.heappop(heap)
