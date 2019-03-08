class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
        if word is None or len(word) == 0:
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        tmp, board[i][j] = board[i][j], '#'
        res = self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i - 1, j) \
        or self.dfs(board, word[1:], i, j + 1) or self.dfs(board, word[1:], i, j - 1)
        board[i][j] = tmp
        return res


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True

        return False

    def dfs(self, board, word, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if len(word) == 1 and board[i][j] == word[0]:
            return True

        if board[i][j] != word[0]:
            return False

        res = False
        board[i][j], tmp = '#', board[i][j]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                continue
            res = res or self.dfs(board, word[1:], x, y)
        board[i][j] = tmp
        return res
