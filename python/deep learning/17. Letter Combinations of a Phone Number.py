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


# dfs
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or len(digits) == 0:
            return []

        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num+1, string+letter, res)

        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }

        res = []
        length = len(digits)
        dfs(0, '', res)
        return res
