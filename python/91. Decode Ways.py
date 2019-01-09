class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0 or int(s[0]) == 0:
            return 0

        dp = [1, 1]
        for i in range(2, len(s) + 1):
            tmp = int(s[i - 2: i])
            if 10 < tmp <= 26 and int(s[i - 1]) != 0:
                dp.append(dp[i - 1] + dp[i - 2])
            elif tmp == 10 or tmp == 20:
                dp.append(dp[i - 2])
            elif int(s[i - 1]) != 0:
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[-1]
        
