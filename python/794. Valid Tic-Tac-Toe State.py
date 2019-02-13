class Solution:
    def is_win(self, board, c):
        for i in range(3):
            if board[i] == c * 3:
                return True
        for i in range(3):
            if board[0][i] == c and board[1][i] == c and board[2][i] == c:
                return True
        if board[0][0] == c and board[1][1] == c and board[2][2] == c:
            return True
        if board[0][2] == c and board[1][1] == c and board[2][0] == c:
            return True
        return False

    def validTicTacToe(self, board: 'List[str]') -> 'bool':
        x_count = o_count = 0
        for i in range(3):
            for j in range(3):
                x_count += 1 if board[i][j] == 'X' else 0
                o_count += 1 if board[i][j] == 'O' else 0

        x_win = self.is_win(board, 'X')
        o_win = self.is_win(board, 'O')

        if x_count < o_count or x_count - o_count > 1:
            return False
        if x_win and o_win:
            return False
        if x_win and x_count == o_count:
            return False
        if o_win and x_count != o_count:
            return False
        return True
