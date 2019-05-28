class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T is None or len(T) == 0:
            return []
        m = len(T)
        res = [0] * m
        stack = [0]
        for i in range(1, m):
            while stack and T[stack[-1]] < T[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
