class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs is None or len(costs) == 0:
            return 0

        m = len(costs)
        dp = [[float('inf') for _ in range(3)] for _ in range(m + 1)]
        dp[0][0] = dp[0][1] = dp[0][2] = 0
        for i in range(1, m + 1):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
        return min(dp[-1])

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None or len(costs) == 0 or len(costs[0]) == 0:
            return 0

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])

        return min(costs[-1][0], costs[-1][1], costs[-1][2])
