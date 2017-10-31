class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) < 3:
            return 0

        start, end = 0, len(height) - 1
        left_most = right_most = res = 0
        while start < end:
            if height[start] <= height[end]:
                left_most = max(left_most, height[start])
                res += left_most - height[start]
                start += 1
            else:
                right_most = max(right_most, height[end])
                res += right_most - height[end]
                end -= 1
        return res
