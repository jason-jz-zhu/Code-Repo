class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        resultMax = 0
        low = sys.maxint
        for price in prices:
            if price -low > resultMax:
                resultMax = price - low
            if price < low:
                low = price
        return resultMax