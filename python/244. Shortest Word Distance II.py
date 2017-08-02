class WordDistance(object):
    import collections
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.hashmap = collections.defaultdict(list)
        for i in xrange(len(words)):
            self.hashmap[words[i]].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indexes1 = self.hashmap[word1]
        indexes2 = self.hashmap[word2]

        i, j, res = 0, 0, sys.maxint
        while i < len(indexes1) and j < len(indexes2):
            res = min(res, abs(indexes1[i] - indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
