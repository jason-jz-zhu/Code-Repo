class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, w * h)
            stack.append(i)
        return max_area


# 2025


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


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0
        
        def calculateArea(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end)
            )
        
        return calculateArea(heights, 0, len(heights) - 1)    
    
# time limit exceeded
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0
        res = float('-inf')
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                res = max(res, (j - i + 1) * min_height)
        return res
