# accept and bfs
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        psList = []
        i = 1
        while i * i <= n:
            psList.append(i * i)
            i += 1
        res = 0
        toCheck = [n]
        while toCheck:
            res += 1
            tmp = set()
            for x in toCheck:
                for y in psList:
                    if x == y:
                        return res
                    if x < y:
                        break
                    tmp.add(x - y)
            toCheck = tmp
        return res
        
# not accept and dp
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint] * (n + 1)

        for i in xrange(n+1):
            if i * i <= n:
                dp[i * i] = 1

        for i in xrange(n+1):
            for j in xrange(n+1):
                if i + j * j <= n:
                    dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])

        return dp[n]
