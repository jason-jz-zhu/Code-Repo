class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        return sum([max(prices[i] - prices[i - 1], 0) for i in xrange(1, len(prices))])
