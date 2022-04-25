class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def update(i, j, box_id, num, flag):
            rows[i][num] = flag
            cols[j][num] = flag
            boxes[box_id][num] = flag
        
        def is_valid(i, j, box_id, num):
            return rows[i][num] == 0 and cols[j][num] == 0 and boxes[box_id][num] == 0
        
        rows = [collections.defaultdict(int) for _ in range(9)]
        cols = [collections.defaultdict(int) for _ in range(9)]
        boxes = [collections.defaultdict(int) for _ in range(9)]
            
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_id = i // 3 * 3 + j //  3
                    update(i, j, box_id, int(board[i][j]), 1)
        
        def fill(i, j):
            if i == 9:
                return True

            next_j = (j + 1) % 9
            next_i = i if next_j != 0 else i + 1
            
            if board[i][j] != '.':
                return fill(next_i, next_j)
            else:
                for d in range(1, 10):
                    box_id = i // 3 * 3 + j //  3
                    if is_valid(i, j, box_id, d):
                        update(i, j, box_id, d, 1)
                        board[i][j] = str(d)
                        if fill(next_i, next_j):
                            return True
                        
                        board[i][j] = '.'
                        update(i, j, box_id, d, 0)
            return False
                        
                        
        fill(0, 0)



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        self.rows = [defaultdict(int) for _ in range(9)]
        self.cols = [defaultdict(int) for _ in range(9)]
        self.boxes = [defaultdict(int) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_index = i // 3 * 3 + j // 3
                    self.update(i, j, box_index, int(board[i][j]), 1)

        self.dfs(board, 0, 0)

    def dfs(self, board, i, j):
        if i == 9:
            return True

        nj = (j + 1) % 9
        ni = i if nj != 0 else i + 1

        if board[i][j] != '.':
            return self.dfs(board, ni, nj)

        for d in range(1, 10):
            box_index = i // 3 * 3 + j // 3
            if not self.is_valid(i, j, box_index, d):
                continue
            self.update(i, j, box_index, d, 1)
            board[i][j] = str(d)
            if self.dfs(board, ni, nj):
                return True
            board[i][j] = '.'
            self.update(i, j, box_index, d, 0)
        return False

    def update(self, i, j, box_index, d, flag):
        self.rows[i][d] = flag
        self.cols[j][d] = flag
        self.boxes[box_index][d] = flag

    def is_valid(self, i, j, box_index, d):
        return self.rows[i][d] == 0 and self.cols[j][d] == 0 and self.boxes[box_index][d] == 0

            
