class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        size = len(prices)
        f1 = [0] * size
        f2 = [0] * size

        min_v = prices[0]
        for i in range(1, size):
            f1[i] = max(f1[i - 1], prices[i] - min_v)
            min_v = min(min_v, prices[i])

        max_v = prices[size - 1]
        for i in range(size - 2, -1, -1):
            f2[i] = max(f2[i + 1], max_v - prices[i])
            max_v = max(max_v, prices[i])

        res = 0
        for i in range(size):
            if f1[i] + f2[i] > res:
                res = f1[i] + f2[i]
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0
        m = len(prices)
        dp = [[0 for _ in range(5)] for _ in range(m + 1)]
        for j in range(1, 5):
            dp[0][j] = float('-inf')

        for i in range(1, m + 1):
            # 0, 2, 4 ...
            for j in range(0, 5, 2):
                dp[i][j] = dp[i - 1][j]
                if i > 1 and j > 1 and dp[i - 1][j - 1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            # 1, 3, 5 ...
            for j in range(1, 5, 2):
                dp[i][j] = dp[i - 1][j - 1]
                if i > 1 and dp[i - 1][j - 1] != float('-inf'):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])

        res = 0
        for j in range(0, 5, 2):
            res = max(res, dp[-1][j])
        return res
                    
