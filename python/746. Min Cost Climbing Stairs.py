class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        size = len(cost)
        dp = [0] * size
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, size):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[size - 1], dp[size - 2])


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        size = len(cost)
        a = cost[0]
        b = cost[1]
        for i in range(2, size):
            tmp = cost[i] + min(a, b)
            a = b
            b = tmp
        return min(a, b)
