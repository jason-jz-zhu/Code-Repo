class Solution(object):
    def minCost(self, costs):
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
