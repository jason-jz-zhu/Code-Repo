class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(1, rowIndex + 1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
