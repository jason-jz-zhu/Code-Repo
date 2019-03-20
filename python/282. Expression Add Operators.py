class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, target, 0, '', 0, 0, res)
        return res

    def dfs(self, num, target, start, path, prev, curr_s, res):
        if start == len(num):
            if curr_s == target:
                res.append(path)
            return

        for i in range(start, len(num)):
            sub_str = num[start: i + 1]
            if len(sub_str) > 1 and sub_str[0] == '0':
                break
            d = int(sub_str)
            if start == 0:
                self.dfs(num, target, i + 1, path + sub_str, d, d, res)
            else:
                self.dfs(num, target, i + 1, path + '+' + sub_str, d, curr_s + d, res)
                self.dfs(num, target, i + 1, path + '-' + sub_str, -d, curr_s - d, res)
                self.dfs(num, target, i + 1, path + '*' + sub_str, prev * d, curr_s - prev + prev * d, res)
