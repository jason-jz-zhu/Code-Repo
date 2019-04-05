class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = float('inf')
        for p in prices:
            res = max(res, p - lowest)
            lowest = min(lowest, p)
        return res
