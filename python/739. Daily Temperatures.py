# stack
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if temperatures is None or len(temperatures) == 0:
            return []

        stack = []
        size = len(temperatures)
        res = [0] * size
        for i in range(size):
            if not stack:
                stack.append((temperatures[i], i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    idx = stack[-1][1]
                    res[idx] = i - idx
                    stack.pop()
                stack.append((temperatures[i], i))
        return res
