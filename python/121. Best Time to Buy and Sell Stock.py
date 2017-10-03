class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        res = 0
        low = sys.maxint
        for price in prices:
            if price - low > res:
                res = price - low
            if price < low:
                low = price
        return res
