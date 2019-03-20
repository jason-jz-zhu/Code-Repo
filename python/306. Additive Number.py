class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        return self.dfs(num, 0, [])

    def dfs(self, num, start, path):
        if start == len(num) and len(path) > 2:
            return True
        
        for i in range(start, len(num)):
            sub_str = num[start: i + 1]
            if len(sub_str) > 1 and sub_str[0] == '0':
                break
            d = int(sub_str)
            if len(path) >= 2:
                s = sum(path[-2:])
                if d > s:
                    break
                elif d < s:
                    continue
            if self.dfs(num, i + 1, path + [d]):
                return True
        return False
