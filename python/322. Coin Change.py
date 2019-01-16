class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [float('inf') for _ in range(amount + 1)]
        f[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    f[i] = min(f[i], f[i - coins[j]] + 1)
        return -1 if f[-1] == float('inf') else f[-1]
