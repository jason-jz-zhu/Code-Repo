class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if words is None or len(words) < 2:
            return -1
        size = len(words)
        l1, l2 = size, -size
        res = float("inf")

        for i in range(size):
            if words[i] == word1:
                l1 = i
            elif words[i] == word2:
                l2 = i
            res = min(res, abs(l1 - l2))
        return res
