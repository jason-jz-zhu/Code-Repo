class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(i):
            nonlocal ans
            if i == n:
                ans += 1
                return
            
            for j in range(n):
                curr_diagonal = i - j
                curr_anti_diagonal = i + j
                if (j in cols 
                    or curr_diagonal in diagonals 
                    or curr_anti_diagonal in anti_diagonals):
                    continue
                
                cols.add(j)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                backtrack(i + 1)
                
                cols.remove(j)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
            
        cols, diagonals, anti_diagonals = set(), set(), set()
        ans = 0
        
        backtrack(0)
        
        return ans


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cols = [False] * n
        self.diag = [False] * (2 ** n - 1)
        self.anti_diag = [False] * (2 ** n - 1)
        self.res = 0
        self.dfs(n, 0, [])
        return self.res

    def dfs(self, n, i, path):
        if i == n:
            self.res += 1
            return

        for j in range(n):
            if not self.is_valid(i, j, n):
                continue
            tmp = "." * n
            self.update(i, j, n, True)
            self.dfs(n, i + 1, path + [tmp[:j] + 'Q' + tmp[j + 1:]])
            self.update(i, j, n, False)

    def is_valid(self, i, j, n):
        return not self.cols[j] and not self.diag[i + j] and not self.anti_diag[i - j + n - 1]

    def update(self, i, j, n, flag):
        self.cols[j] = flag
        self.diag[i + j] = flag
        self.anti_diag[i - j + n - 1] = flag
