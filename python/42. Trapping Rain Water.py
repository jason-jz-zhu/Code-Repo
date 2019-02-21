
# montone decreate stack
class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if height is None or len(height) < 3:
            return 0

        stack = []
        i = 0
        res = 0
        while i < len(height):
            if not stack or height[stack[-1]] > height[i]:
                stack.append(i)
                i += 1
            else:
                lowest = stack.pop()
                if not stack:
                    continue
                h = min(height[i], height[stack[-1]]) - height[lowest]
                w = i - stack[-1] - 1
                res += h * w
        return res



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) < 3:
            return 0

        res = 0
        left = [0] * len(height)
        left[0] = 0
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i - 1])

        right = 0
        for i in range(len(height) - 1, -1, -1):
            if min(left[i], right) - height[i] > 0:
                res += min(left[i], right) - height[i]
            right = max(right, height[i])

        return res



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
