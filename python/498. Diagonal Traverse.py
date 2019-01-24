class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        hashmap = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                hashmap[i + j].append(matrix[i][j])

        for k in range(m + n - 1):
            if k % 2 == 0:
                res += hashmap[k][::-1]
            else:
                res += hashmap[k]
        return res
