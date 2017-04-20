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

# accept and bfs
class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt
