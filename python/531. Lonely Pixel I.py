class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if picture is None or len(picture) == 0 or len(picture[0]) == 0:
            return 0

        row, col = len(picture), len(picture[0])
        row_check, col_check = row * [0], col * [0]
        res = 0
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    row_check[i] += 1
                    col_check[j] += 1

        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    if row_check[i] == 1 and col_check[j] == 1:
                        res += 1

        return res
