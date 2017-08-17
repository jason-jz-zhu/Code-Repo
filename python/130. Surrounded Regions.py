class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        q = collections.deque([])

        for i in xrange(len(board)):
            q.append((i, 0))
            q.append((i, len(board[0]) - 1))
        for j in xrange(len(board[0])):
            q.append((0, j))
            q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()
            if board[i][j] == 'O':
                board[i][j] = 'Y'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                        q.append((x, y))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
