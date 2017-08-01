class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if picture is None or len(picture) == 0:
            return 0
        m, n = len(picture), len(picture[0])
        row, col = [0] * m, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        import collections
        hashmap = collections.defaultdict(int)
        for r in picture:
            hashmap[''.join(r)] += 1

        res = 0
        for i in xrange(m):
            tmpR = ''.join(picture[i])
            if hashmap[tmpR] != N:
                continue
            for j in xrange(n):
                if picture[i][j] == 'B':
                    if row[i] == N and col[j] == N:
                        res += 1
        return res
