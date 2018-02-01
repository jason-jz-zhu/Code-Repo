class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None or len(words) == 0:
            return 0
        res = 0
        mask = [0] * len(words)
        for i in range(len(words)):
            for c in words[i]:
                mask[i] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not (mask[i] & mask[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
