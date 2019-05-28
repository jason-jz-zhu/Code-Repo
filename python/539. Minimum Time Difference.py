class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if timePoints is None or len(timePoints) == 0:
            return 0
        minutes = [int(t[: 2]) * 60 + int(t[3:]) for t in timePoints]
        minutes.sort()
        res = float('inf')
        for i in range(1, len(minutes)):
            d = abs(minutes[i] - minutes[i - 1])
            res = min(res, d)
        return min(res, 24 * 60 + minutes[0] - minutes[-1])
