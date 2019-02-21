class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        if not board[0] or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = self.count_around_live(board, i, j)
                if board[i][j]:
                    if cnt not in (2, 3):
                        board[i][j] = 2
                else:
                    if cnt == 3:
                        board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2

    def count_around_live(self, board, i, j):
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in range(8):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                continue
            if board[x][y] == 1 or board[x][y] == 2:
                cnt += 1
        return cnt
