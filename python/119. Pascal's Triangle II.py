
class Solution:
    def __init__(self):
        self.cache = {}
        
    def getNum(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        if (row, col) in self.cache:
            return self.cache[(row, col)]
        left = self.getNum(row - 1, col - 1)
        self.cache[(row - 1, col - 1)] = left
        right = self.getNum(row - 1, col)
        self.cache[(row - 1, col)] = right
        return left + right
    
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex + 1):
            res.append(self.getNum(rowIndex, i))
        return res
    
 class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = [1]
        for r in range(1, rowIndex + 1):
            curr = [1]
            for i in range(1, len(prev)):
                curr.append(prev[i] + prev[i-1])
            curr.append(1)
            prev = curr
            
        return curr


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
