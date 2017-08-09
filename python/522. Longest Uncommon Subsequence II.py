class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(x, y):
            i = j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                j += 1
            return i == len(x)

        res = -1
        for i in xrange(len(strs)):
            for j in xrange(len(strs)):
                if i == j:
                    continue
                if isSubsequence(strs[i], strs[j]):
                    if j == len(strs) - 1:
                        j = 0
                    break
            print j, len(strs)
            if j == len(strs) - 1:
                res = max(res, len(strs[i]))
        return res

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSubsequence(x, y):
            i = j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    i += 1
                j += 1
            return i == len(x)

        strs.sort(key=len, reverse=True)
        for i in xrange(len(strs)):
            flag = True
            for j in xrange(len(strs)):
                if i == j:
                    continue
                if isSubsequence(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                return len(strs[i])
        return -1
