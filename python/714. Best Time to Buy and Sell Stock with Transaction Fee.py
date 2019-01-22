class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        sold = 0
        hold = -prices[0]
        for price in prices[1:]:
            sold = max(sold, hold + price - fee)
            hold = max(hold, sold - price)
        return sold
