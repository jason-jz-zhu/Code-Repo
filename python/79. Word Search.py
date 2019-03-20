class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[0]:
            return False
        board[i][j], tmp = '#', board[i][j]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if self.dfs(board, word[1:], x, y):
                return True
        board[i][j] = tmp
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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

        board[i][j], tmp = '#', board[i][j]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                continue
            if self.dfs(board, word[1:], x, y):
                return True
        board[i][j] = tmp
        return False
