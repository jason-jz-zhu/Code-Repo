class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        i1, i2 = size, -size
        res = sys.maxint
        for i in range(size):
            if words[i] == word1:
                i1 = i2 if word1 == word2 else i
            if words[i] == word2:
                i2 = i
            res = min(res, abs(i1 - i2))

        return res
