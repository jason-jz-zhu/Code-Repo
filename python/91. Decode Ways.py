class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        m = len(s)
        dp = [0 for _ in range(m + 1)]
        dp[0] = 1
        for i in range(1, m + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i >= 2 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                dp[i] += dp[i - 2]

        return dp[-1]
