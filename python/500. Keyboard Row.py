class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if words is None or len(words) == 0:
            return []
        res = []
        row1, row2, row3 = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        # main loop
        for word in words:
            word_set = set(word)
            c1 = c2 = c3 = 0
            for w in word_set:
                if w.lower() in row1: c1 = 1
                if w.lower() in row2: c2 = 1
                if w.lower() in row3: c3 = 1
                if c1 + c2 + c3 > 1: break
            if c1 + c2 + c3 == 1:
                res.append(word)
        return res
