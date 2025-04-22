class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            res = max(res, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res