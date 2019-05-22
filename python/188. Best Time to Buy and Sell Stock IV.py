class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        m = len(prices)

        if k > m / 2:
            s = 0
            for i in range(1, m):
                s += max(0, prices[i] - prices[i - 1])
            return s


        dp = [[0 for _ in range(k * 2 + 1)] for _ in range(2)]
        for j in range(1, k * 2 + 1):
            dp[0][j] = float('-inf')
        now, old = 0, 1
        for i in range(1, m + 1):
            now, old = old, now
            # 0, 2, 4 .....
            for j in range(0, k * 2 + 1, 2):
                dp[now][j] = dp[old][j]
                if i > 0 and j > 0 and dp[old][j - 1] != float('-inf'):
                    dp[now][j] = max(dp[now][j], dp[old][j - 1] + prices[i - 1] - prices[i -2])

            # 1, 3, 5 ...
            for j in range(1, k * 2 + 1, 2):
                dp[now][j] = dp[old][j - 1]
                if i > 0 and dp[old][j] != float('-inf'):
                    dp[now][j] = max(dp[now][j], dp[old][j] + prices[i - 1] - prices[i -2])

        res = 0
        for j in range(0, k * 2 + 1, 2):
            res = max(res, dp[now][j])
        return res
