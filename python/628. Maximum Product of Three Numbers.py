class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return None

        max1 = max2 = max3 = -sys.maxint - 1
        min1 = min2 = sys.maxint

        for num in nums:
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

        return max(min1 * min2 * max1, max1 * max2 * max3)
