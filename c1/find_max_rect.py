# 3. input = [1,2,3,2,1],数组的值代表高度，index表示连续的横坐标，
# 在这个范围内找到最大的正方形，比如这样，答案是4

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