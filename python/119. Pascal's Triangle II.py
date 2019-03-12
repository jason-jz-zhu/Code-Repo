class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(1, rowIndex + 1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row



class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex - 1)
        row = []
        for i in range(rowIndex + 1):
            if i == 0 or i == rowIndex:
                row.append(1)
            else:
                row.append(last[i - 1] + last[i])
        return row
