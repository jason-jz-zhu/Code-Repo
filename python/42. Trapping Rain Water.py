class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        n = len(height)
        res = 0
        l_max = [0] * n
        r_max = [0] * n
        l_max[0] = height[0]
        r_max[n - 1] = height[n - 1]
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        for j in range(n - 2, -1, -1):
            r_max[j] = max(height[j], r_max[j + 1])

        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max = 0, 0
        res = 0

        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res

# -----

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




