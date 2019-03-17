class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if not num or len(num) == 0:
            return False
        return self.dfs(num, 0, [])

    def dfs(self, num, index, path):
        if index == len(num) and len(path) >= 3:
            return True

        for i in range(index, len(num)):
            substr = num[index: i + 1]
            if len(substr) > 1 and substr[0] == '0':
                break
            d = int(substr)
            if len(path) >= 2:
                s = sum(path[-2:])
                if d > s:
                    break
                elif d < s:
                    continue
            if self.dfs(num, i + 1, path + [d]):
                return True
        return False
                
