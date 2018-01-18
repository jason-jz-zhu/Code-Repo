class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        if not board[0] or len(board[0]) == 0:
            return

        q = collections.deque([])
        for i in range(len(board)):
            q.append((i, 0))
            q.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            q.append((0, j))
            q.append((len(board) - 1, j))

        dir_x, dir_y = [-1, 0, 0, 1], [0, 1, -1, 0]
        while q:
            x, y = q.popleft()
            if board[x][y] == 'O':
                board[x][y] = 'Y'
                for k in range(4):
                    board_x, board_y = x + dir_x[k], y + dir_y[k]
                    if board_x < 0 or board_x >= len(board) or board_y < 0 or board_y >= len(board[0]):
                        continue
                    if board[board_x][board_y] == 'O':
                        q.append((board_x, board_y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
