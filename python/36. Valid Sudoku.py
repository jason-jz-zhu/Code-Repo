class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                box_index = (i // 3) * 3 + j // 3
                num = int(num)
                rows[i][num] += 1
                cols[j][num] += 1
                boxes[box_index][num] += 1

                if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                    return False

        return True
