class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, index, cur, res):
        if len(cur) == 4:
            if index == len(s):
                res.append('.'.join(cur))
            return

        for i in xrange(index, index + 3):
            if len(s) > i and self.isValidNum(s[index: i + 1]):
                self.dfs(s, i + 1, cur + [s[index: i + 1]], res)

    def isValidNum(self, s):
        if len(s) == 0 or len(s) > 3:
            return False
        if s[0] == '0' and len(s) != 1:
            return False
        if len(s) == 3 and int(s) > 255:
            return False
        return True
