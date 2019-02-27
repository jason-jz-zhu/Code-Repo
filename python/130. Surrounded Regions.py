class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.bfs(board, i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m - 1][j] == 'O':
                self.bfs(board, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def bfs(self, board, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        q = collections.deque([(i, j)])
        board[i][j] = 'Y'
        while q:
            board_x, board_y = q.popleft()
            for k in range(4):
                x, y = board_x + dx[k], board_y + dy[k]
                if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                    continue
                if board[x][y] == 'O':
                    board[x][y] = 'Y'
                    q.append((x, y))


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited)
            if board[i][n - 1] == 'O':
                self.dfs(board, i, n - 1, visited)
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, visited)
            if board[m - 1][j] == 'O':
                self.dfs(board, m - 1, j, visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def dfs(self, board, i, j, visited):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or board[i][j] != 'O':
            return
        board[i][j] = 'Y'
        visited.add((i, j))
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            self.dfs(board, x, y, visited)
