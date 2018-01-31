class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0 or num > 10:
            return []

        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append('{:d}:{:02d}'.format(h, m))
        return res

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0 or num > 10:
            return []

        res = []
        hour = [8, 4, 2, 1]
        minute = [32, 16, 8, 4, 2, 1]
        for i in range(num + 1):
            hours = self.helper(hour, i)
            minutes = self.helper(minute, num - i)
            for h in hours:
                if h > 11:
                    continue
                for m in minutes:
                    if m > 59:
                        continue
                    res.append('{:d}:{:02d}'.format(h, m))
        return res

    def helper(self, nums, cnt):
        res = []
        self.dfs(nums, cnt, 0, 0, res)
        return res

    def dfs(self, nums, cnt, index, cache, res):
        if cnt == 0:
            res.append(cache)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, cnt - 1, i + 1, cache + nums[i], res)
