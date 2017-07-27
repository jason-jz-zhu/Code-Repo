class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        smallest = secondSmallest = sys.maxint

        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= secondSmallest:
                secondSmallest = num
            else:
                return True
        return False
