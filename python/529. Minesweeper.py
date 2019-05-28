class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        q = collections.deque([click])
        while q:
            row, col = q.popleft()
            if board[row][col] == 'M':
                board[row][col] = 'X'
            else:
                count = 0
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        r, c = row + i, col + j
                        if not (0 <= r < len(board)) or not (0 <= c < len(board[r])):
                            continue
                        if board[r][c] == 'M' or board[r][c] == 'X':
                            count += 1

                if count:
                    board[row][col] = chr(count + ord('0'))
                else:
                    board[row][col] = 'B'
                    for i in xrange(-1, 2):
                        for j in xrange(-1, 2):
                            if i == 0 and j == 0:
                                continue
                            r, c = row + i, col + j
                            if not (0 <= r < len(board)) or not (0 <= c < len(board[r])):
                                continue
                            if board[r][c] == 'E':
                                q.append((r, c))
                                board[r][c] = ' '

        return board


# Time:  O(m * n)
# Space: O(m * n)
# dfs
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or len(board) == 0:
            return []

        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        if board[i][j] != 'E':
            return
        m, n = len(board), len(board[0])
        directions = []
        for ii in range(-1, 2):
            for jj in range(-1, 2):
                if ii == 0 and jj == 0:
                    continue
                directions.append((ii, jj))
        cnt = 0
        for dir in directions:
            dx, dy = i + dir[0], j + dir[1]
            if dx < 0 or dx >= m or dy < 0 or dy >= n:
                continue
            if board[dx][dy] == 'M':
                cnt += 1

        if cnt != 0:
            board[i][j] = str(cnt)
            return
        board[i][j] = 'B'
        for dir in directions:
            dx, dy = i + dir[0], j + dir[1]
            if dx < 0 or dx >= m or dy < 0 or dy >= n:
                continue
            self.dfs(board, dx, dy)
