class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words is None or len(words) == 0:
            return ''

        res = ''
        prev = set([''])
        for word in sorted(words):
            if word[:-1] in prev:
                prev.add(word)
                res = max(res, word, key=len)
        return res
