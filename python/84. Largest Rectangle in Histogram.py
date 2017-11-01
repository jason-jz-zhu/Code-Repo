class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        res = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        height.pop()
        return res    
