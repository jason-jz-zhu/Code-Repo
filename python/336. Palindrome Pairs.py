class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if words is None or len(words) == 0:
            return []
        res = []
        hashmap = {}
        for i, word in enumerate(words):
            hashmap[word] = i

        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][:j]
                suffix = words[i][j:]
                if j > 0 and prefix == prefix[::-1] and \
                    suffix[::-1] in hashmap and hashmap[suffix[::-1]] != i:
                        res.append([hashmap[suffix[::-1]], i])
                if suffix == suffix[::-1] and \
                    prefix[::-1] in hashmap and hashmap[prefix[::-1]] != i:
                        res.append([i, hashmap[prefix[::-1]]])
        return res
