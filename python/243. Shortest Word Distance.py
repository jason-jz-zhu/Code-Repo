class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        i1 = i2 = size
        res = size + 1

        for i in xrange(size):
            if words[i] == word1:
                i1 = i
                res = min(res, abs(i1 - i2))
            elif words[i] == word2:
                i2 = i
                res = min(res, abs(i1 - i2))
        return res
        
