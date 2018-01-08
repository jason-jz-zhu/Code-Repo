class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        idx = [0] * len(primes)
        while len(res) < n:
            tmp = []
            mm = float('inf')
            for i in range(len(primes)):
                tmp.append(res[idx[i]] * primes[i])
            for i in range(len(primes)):
                mm = min(mm, tmp[i])
            for i in range(len(primes)):
                if mm == tmp[i]:
                    idx[i] += 1
            res.append(mm)
        return res[-1]
