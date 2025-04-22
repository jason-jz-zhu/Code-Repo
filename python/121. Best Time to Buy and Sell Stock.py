class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        df = [[0, 0] for i in range(n)]
        for i in range(n):
            if i - 1 == -1:
                df[i][0] = 0
                df[i][1] = -prices[i]
                continue
            df[i][0] = max(df[i-1][0], df[i-1][1] + prices[i])
            df[i][1] = max(df[i-1][1], -prices[i])
        return df[n-1][0]








class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = float('inf')
        for p in prices:
            res = max(res, p - lowest)
            lowest = min(lowest, p)
        return res
