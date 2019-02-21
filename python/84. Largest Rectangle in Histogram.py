class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        res = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        if not heights or len(heights) == 0:
            return 0
        heights.append(0)
        stack = []
        res = 0
        i = 0
        while i < len(heights):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                h_index = stack.pop()
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                h = heights[h_index]
                res = max(res, w * h)
        return res
