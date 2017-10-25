class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
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
