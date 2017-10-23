class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []

        hashmap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        self.dfs(digits, hashmap, 0, '', res)
        return res

    def dfs(self, digits, hashmap, num, path, res):
        if num == len(digits):
            res.append(path)
            return
        for letter in hashmap[int(digits[num])]:
            self.dfs(digits, hashmap, num + 1, path + letter, res)



class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []

        chr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        for i in xrange(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in xrange(0, len(chr[num])):
                if len(res):
                    for k in xrange(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(chr[num][j])
            res = copy.copy(tmp)

        return res
