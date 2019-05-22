class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if costs is None or len(costs) == 0:
            return 0

        m = len(costs)
        K = len(costs[0])

        dp = [[float('inf') for _ in range(K)] for _ in range(m + 1)]

        for j in range(K):
            dp[0][j] = 0

        for i in range(1, m + 1):
            f = s = -1
            for k in range(K):
                if f == -1 or dp[i - 1][k] < dp[i - 1][f]:
                    s = f
                    f = k
                elif s == -1 or dp[i - 1][k] < dp[i - 1][s]:
                    s = k

            for j in range(K):
                if j != f:
                    dp[i][j] = dp[i - 1][f] + costs[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][s] + costs[i - 1][j]

        return min(dp[m])


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None or len(costs) == 0:
            return 0

        size = len(costs)
        k = len(costs[0])

        for i in range(1, size):
            for j in range(k):
                exclude = costs[i - 1][j]
                costs[i - 1][j] = sys.maxint
                costs[i][j] += min(costs[i - 1])
                costs[i - 1][j] = exclude
        return min(costs[-1])
