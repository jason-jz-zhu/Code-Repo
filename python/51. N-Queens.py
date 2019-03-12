class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.cols = [False] * n
        self.diag = [False] * (2 ** n - 1)
        self.anti_diag = [False] * (2 ** n - 1)
        res = []
        self.dfs(n, 0, [], res)
        return res

    def dfs(self, n, i, path, res):
        if i == n:
            res.append(path)
            return

        for j in range(n):
            if not self.is_valid(i, j, n):
                continue
            tmp = "." * n
            self.update(i, j, n, True)
            self.dfs(n, i + 1, path + [tmp[:j] + 'Q' + tmp[j + 1:]], res)
            self.update(i, j, n, False)

    def is_valid(self, i, j, n):
        return not self.cols[j] and not self.diag[i + j] and not self.anti_diag[i - j + n - 1]

    def update(self, i, j, n, flag):
        self.cols[j] = flag
        self.diag[i + j] = flag
        self.anti_diag[i - j + n - 1] = flag
