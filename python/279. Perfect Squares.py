class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        for a in range(int(n ** 0.5) + 1):
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
        return 3

            

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
        stack = [n]
        while stack:
            res += 1
            tmp = set()
            for x in stack:
                for y in psList:
                    if x == y:
                        return res
                    if x < y:
                        break
                    tmp.add(x - y)
            stack = tmp
        return res
