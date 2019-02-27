class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return False
        i = 0
        m = len(bits)
        while i < m:
            if i == m - 1:
                return True
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return False


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if not bits:
            return False
        return self.dfs(bits, 0)

    def dfs(self, bits, index):
        if index >= len(bits):
            return False
        if index == len(bits) - 1:
            return True
        if bits[index] == 1:
            return self.dfs(bits, index + 2)
        else:
            return self.dfs(bits, index + 1)
